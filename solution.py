assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """
    Eliminate values using the naked twins strategy.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        unsolved_boxes = [box for box in unit if len(values[box]) > 1]

        # Create dictionary where the available values are the keys and a list of
        # the corresponding boxes that have those values are the values of the
        # dictionary.
        values_dict = {}

        for box in unsolved_boxes:
            values_dict.setdefault(values[box], [])
            values_dict[values[box]].append(box)

        # find value sets that have the same number of boxes as the length of the
        # value set. Note: this handles naked triplets and quadruplets as well.
        naked_sets = [s for s in values_dict.keys() if len(s) == len(values_dict[s])]

        for naked_set in naked_sets:
            other_boxes = [box for box in unsolved_boxes if box not in values_dict[naked_set]]

            for box in other_boxes:
                for val in naked_set:
                    new_value = values[box].replace(val, '')
                    if new_value != values[box]:
                        assign_value(values, box, new_value)

    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    # Using the same code as was used in the Udacity course content/quizzes
    return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid) == 81, "Must have 81 characters in grid string"
    unsolved_string = '123456789'
    grid_list = [x if x != '.' else unsolved_string for x in list(grid)]
    return dict(zip(boxes, grid_list))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        Nothing
    """
    # Using the same code as was used in the Udacity course content/quizzes
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r+c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Find boxes which have already been solved, i.e. only have a single value
    and eliminate that value from any of its peers.

    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        The dictionary representation of the resulting sudoku grid.
    """
    for key, val in values.items():
        if len(val) == 1:
            for peer in peers[key]:
                new_value = values[peer].replace(val, '')
                if new_value != values[peer]:
                    assign_value(values, peer, new_value)

    return values

def only_choice(values):
    """
    Isolate and options that are the only choice for a unit and assign them.

    Args:
        values(dict): The sudokue in dictionary form
    Returns:
        The dictionary representation of the resulting sudoku grid.
    """
    for unit in unitlist:
        unsolved_boxes = [box for box in unit if len(values[box]) > 1]

        for box in unsolved_boxes:
            box_set = set(values[box])
            other_boxes = [b for b in unit if b != box] #Don't want to consider itself.

            for b in other_boxes:
                box_set = box_set - set(values[b])

            if len(box_set) == 1:
                assign_value(values, box, box_set.pop())

    return values

def solved_value_count(values):
    """
    Deterine how many boxes have been solved, i.e. reduced to a single value.

    Args:
        values(dict): The sudoku in dictionary form.
    Returns:
        An integer represneting the number of boxes that have been solved.
    """
    return len([box for box in values.keys() if len(values[box]) == 1])


def reduce_puzzle(values):
    """
    Repeatedly apply the eliminate and only_choice strategies until either the
    puzzle is solved or can't be reduced further.

    Args:
        values(dict): The sudokue in dictionary form
    Returns:
        The dictionary representation of the resulting sudoku grid.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = solved_value_count(values)

        # Apply solving strategies
        eliminate(values)
        only_choice(values)
        naked_twins(values)

        solved_values_after = solved_value_count(values)
        stalled = solved_values_before == solved_values_after

        # I think this could only arise when fed an invalid values state, e.g.
        # multiple boxes reduced to the same single digit within a unit. Keeping
        # for consistency and guarding.
        #
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values

def search(values):
    """
    Using depth-first search and propagation, create a search tree and solve the sudoku.

    Args:
        values(dict): The sudokue in dictionary form
    Returns:
        The dictionary representation of the resulting sudoku grid.
    """
    values = reduce_puzzle(values)

    if values is False:
        return False

    unsolved_boxes = [box for box in values if len(values[box]) > 1]

    if len(unsolved_boxes) == 0:
        return values #already solved

    # Branch search on the box with the fewest digits
    branch_box = sorted(unsolved_boxes, key=lambda box: len(values[box]))[0]

    # Recuresively solve each one of the resulting sudokus, returning the first one
    # to return a value, indicating a solution.
    for digit in values[branch_box]:
        branched_values = values.copy()
        branched_values[branch_box] = digit

        result = search(branched_values)

        if result:
            return result

def solve(grid, diagonal=True):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    setup(diagonal)
    values = grid_values(grid)
    return search(values)

def setup(diagonal=True):
    global boxes
    boxes = cross(rows, cols)

    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    forward_diagonal_unit = [r + str(i+1) for (i, r) in enumerate(rows)]
    reverse_diagonal_unit = [r + str(len(rows) - i) for (i, r) in enumerate(rows)]
    diagonal_units = [forward_diagonal_unit, reverse_diagonal_unit]

    global unitlist
    unitlist = row_units + column_units + square_units

    if diagonal:
        unitlist += diagonal_units

    calculate_units()
    calculate_peers()

def calculate_units():
    global units
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)

def calculate_peers():
    global peers
    peers = dict((s, set(sum(units[s],[])) - set([s])) for s in boxes)

# Handle default setup
setup()

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    values = solve(diag_sudoku_grid)
    display(values)

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
