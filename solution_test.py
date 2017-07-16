import solution
import unittest


class TestNakedTwins(unittest.TestCase):
    before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                            'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                            'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                            'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27',
                            'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
                            'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                            'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6',
                            'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
                            'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27',
                            'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                            'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
    possible_solutions_1 = [
        {'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1',
         'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8',
         'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
         'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4',
         'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
         'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347',
         'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
         'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279',
         'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'},
        {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7',
         'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
         'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9',
         'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
         'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
         'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
         'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
         'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6',
         'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
        ]

    before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                            'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                            'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
                            'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
                            'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
                            'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
                            'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                            'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
                            'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
                            'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
                            'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    possible_solutions_2 = [
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'},
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '3', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    ]

    def test_naked_twins(self):
        self.assertTrue(solution.naked_twins(self.before_naked_twins_1) in self.possible_solutions_1,
                        "Your naked_twins function produced an unexpected board.")

    def test_naked_twins2(self):
        self.assertTrue(solution.naked_twins(self.before_naked_twins_2) in self.possible_solutions_2,
                        "Your naked_twins function produced an unexpected board.")



class TestDiagonalSudoku(unittest.TestCase):
    diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                          'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                          'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                          'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                          'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                          'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                          'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                          'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                          'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                          'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                          'D1': '5'}

    def test_solve(self):
        self.assertEqual(solution.solve(self.diagonal_grid), self.solved_diag_sudoku)

class TestGridValues(unittest.TestCase):
    diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    def test_length_check(self):
        with self.assertRaisesRegex(AssertionError, '81 characters'):
            solution.grid_values('123')

    def test_dict_length(self):
        values = solution.grid_values(self.diagonal_grid)
        self.assertEqual(len(values), 81)

    def test_dict_key_format(self):
        values = solution.grid_values(self.diagonal_grid)
        self.assertTrue('A1' in values.keys())
        self.assertTrue('C6' in values.keys())
        self.assertTrue('I9' in values.keys())

    def test_direct_copy_of_solved_boxes(self):
        values = solution.grid_values(self.diagonal_grid)
        self.assertEqual(values['A1'], '2')
        self.assertEqual(values['B6'], '6')

    def test_unsolved_string_substitution(self):
        values = solution.grid_values(self.diagonal_grid)
        self.assertEqual(values['A2'], '123456789')

class TestEliminate(unittest.TestCase):
    values = {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789', 'A5': '2',
    'A6': '123456789', 'A7': '6', 'A8': '123456789', 'A9': '123456789', 'B1': '9', 'B2': '123456789',
    'B3': '123456789', 'B4': '3', 'B5': '123456789', 'B6': '5', 'B7': '123456789', 'B8': '123456789',
    'B9': '1', 'C1': '123456789', 'C2': '123456789', 'C3': '1', 'C4': '8', 'C5': '123456789', 'C6': '6',
    'C7': '4', 'C8': '123456789', 'C9': '123456789', 'D1': '123456789', 'D2': '123456789', 'D3': '8',
    'D4': '1', 'D5': '123456789', 'D6': '2', 'D7': '9', 'D8': '123456789', 'D9': '123456789', 'E1': '7',
    'E2': '123456789', 'E3': '123456789', 'E4': '123456789', 'E5': '123456789', 'E6': '123456789',
    'E7': '123456789', 'E8': '123456789', 'E9': '8', 'F1': '123456789', 'F2': '123456789', 'F3': '6',
    'F4': '7', 'F5': '123456789', 'F6': '8', 'F7': '2', 'F8': '123456789', 'F9': '123456789',
    'G1': '123456789', 'G2': '123456789', 'G3': '2', 'G4': '6', 'G5': '123456789', 'G6': '9', 'G7': '5',
    'G8': '123456789', 'G9': '123456789', 'H1': '8', 'H2': '123456789', 'H3': '123456789', 'H4': '2',
    'H5': '123456789', 'H6': '3', 'H7': '123456789', 'H8': '123456789', 'H9': '9', 'I1': '123456789',
    'I2': '123456789', 'I3': '5', 'I4': '123456789', 'I5': '1', 'I6': '123456789', 'I7': '3',
    'I8': '123456789', 'I9': '123456789'}

    def test_eliminates_horizontal_peers(self):
        eliminated_values = solution.eliminate(self.values.copy())
        self.assertTrue('3' not in eliminated_values['A1'])
        self.assertTrue('2' not in eliminated_values['A1'])
        self.assertTrue('6' not in eliminated_values['A1'])

    def test_eliminates_vertical_peers(self):
        eliminated_values = solution.eliminate(self.values.copy())
        self.assertTrue('9' not in eliminated_values['A1'])
        self.assertTrue('7' not in eliminated_values['A1'])
        self.assertTrue('8' not in eliminated_values['A1'])

    def test_eliminate_square_peers(self):
        eliminated_values = solution.eliminate(self.values.copy())
        self.assertTrue('1' not in eliminated_values['A1'])
        self.assertTrue('9' not in eliminated_values['A2'])
        self.assertTrue('3' not in eliminated_values['B2'])

    def test_eliminate_preserves_solved_values(self):
        eliminated_values = solution.eliminate(self.values.copy())
        self.assertEqual(eliminated_values['A3'], '3')
        self.assertEqual(eliminated_values['D7'], '9')
        self.assertEqual(eliminated_values['H1'], '8')

class TestOnlyChoice(unittest.TestCase):
    values = {'A1': '45', 'A2': '4578', 'A3': '3', 'A4': '9', 'A5': '2', 'A6': '14', 'A7': '6', 'A8': '5789', 'A9': '57',
    'B1': '9', 'B2': '24678', 'B3': '47', 'B4': '3', 'B5': '47', 'B6': '5', 'B7': '78', 'B8': '278', 'B9': '1',
    'C1': '25', 'C2': '257', 'C3': '1', 'C4': '8', 'C5': '79', 'C6': '6', 'C7': '4', 'C8': '23579', 'C9': '2357',
    'D1': '345', 'D2': '345', 'D3': '8', 'D4': '1', 'D5': '3456', 'D6': '2', 'D7': '9', 'D8': '34567', 'D9': '34567',
    'E1': '7', 'E2': '123459', 'E3': '49', 'E4': '59', 'E5': '34569', 'E6': '4', 'E7': '1', 'E8': '13456', 'E9': '8',
    'F1': '1345', 'F2': '13459', 'F3': '6', 'F4': '7', 'F5': '3459', 'F6': '8', 'F7': '2', 'F8': '1345', 'F9': '345',
    'G1': '134', 'G2': '1347', 'G3': '2', 'G4': '6', 'G5': '8', 'G6': '9', 'G7': '5', 'G8': '1478', 'G9': '47',
    'H1': '8', 'H2': '1467', 'H3': '47', 'H4': '2', 'H5': '5', 'H6': '3', 'H7': '17', 'H8': '1467', 'H9': '9',
    'I1': '6', 'I2': '69', 'I3': '5', 'I4': '4', 'I5': '1', 'I6': '7', 'I7': '3', 'I8': '268', 'I9': '26'}

    def test_only_choice_in_row(self):
        only_choiced_values = solution.only_choice(self.values.copy())
        self.assertEqual(only_choiced_values['B2'], '6')

    def test_only_choice_in_col(self):
        only_choiced_values = solution.only_choice(self.values.copy())
        self.assertEqual(only_choiced_values['E3'], '9')

    def test_only_choice_in_square(self):
        only_choiced_values = solution.only_choice(self.values.copy())
        self.assertEqual(only_choiced_values['A6'], '1')

    def test_only_choice_preserves_solved_values(self):
        only_choiced_values = solution.only_choice(self.values.copy())
        self.assertEqual(only_choiced_values['F4'], '7')

if __name__ == '__main__':
    unittest.main()
