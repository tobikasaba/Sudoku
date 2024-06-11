def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet
    # in the puzzle, representing any open spaces with -1
    # return row, col tuple(or None, None) if there in none)

    # keep in mind that we are using 0-8 for our indices
    pass
def solve_sudoku(puzzle):
    # solve sudoku using backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if the solution exists)


    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)