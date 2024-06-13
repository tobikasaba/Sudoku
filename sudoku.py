def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet
    # in the puzzle, representing any open spaces with -1
    # return row, col tuple(or (None, None) if there is no empty space)

    # keep in mind that we are using 0-8 for our indices
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    # if there are no empty spaces left, i.e -1
    return None, None


def solve_sudoku(puzzle):
    # solve sudoku using backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if the solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, them we're done because we only allowed valid inputs
    if row is None:
        return True
    # step 2: if there is a place to put a number, then make a gues between 1 and 9
    for guess in range(1, 10):
        # step 3: checking ig this is a valid guess
        pass
