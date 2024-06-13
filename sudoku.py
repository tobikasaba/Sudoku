from pprint import pprint


def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet
    # in the puzzle, representing any open spaces with -1
    # return row, col tuple(or (None, None) if there is no empty space)

    # keep in mind that we are using 0-8 for our indices
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    # if there are no empty spaces left, i.e. -1
    return None, None


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is valid
    # returns True if valid and False if not

    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append((puzzle(i)[col]))
    col_vals = [puzzle[i][col] for i in range(9)]

    if guess in col_vals:
        return False

    # the square.
    # first get where 3x3 square starts.
    # split the entire board into 3 chunks of 3x3 squares.
    # iterate over the 3 values in the row/column.
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # iterate over the 3x3 square selected based on the predetermined starting position
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[row][col] == guess:
                return False

    # if we get here, the checks pass
    return True


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
        # step 3: checking if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1 if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle.
            # step 4: recursively call the function
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid OR if our guess does not solve the puzzle,
        # then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle in UNSOLVABLE!!
    return False


if __name__ == "__main__":
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
