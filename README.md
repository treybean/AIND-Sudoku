# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: By reducing the search space to a single unit, we are able to look for n boxes
   within that unit that all have the same available possible values of length n
   and conclude that no other box in that unit can contain those values as possible
   solutions. This is an example of constraint propagation because if we leave the
   search space as the entire board, two boxes, having the same two available value
   doesn't allow us to draw any further conclusions about those, or any other boxes.

   This is a general rule for sudoku, which the naked_twin is a specific example of,
   when n = 2. I added a test for the naked_triplet, where n = 3, to the set of tests
   to verify that scenario is correctly addressed as well.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Similar to the description above, for a given box that lies on the diagonal,
   we are able to limit the search space for the possible values for that box, by
   considering the values of other boxes in the diagonal unit. This reduces the
   amount of boxes that need to be considered to determine available values for that
   box. Further, since we're adding this constraint to the existing unit constraints, e.g.
   row, column, and square, it should further reduce the amount of values available
   for boxes in the diagonal unit, making it easier to solve those boxes. Further,
   by having more boxes solved, it propagates to further constraints when utilizing
   other unit constraints or strategies.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.
