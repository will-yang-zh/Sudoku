
import numpy as np

# Load sudokus
sudoku = np.load("data/medium_puzzle.npy")[14]


fail_board = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1,]
]
domain = [1,2,3,4,5,6,7,8,9]

def empty(sudoku):
    # print(count)
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                temp_domain = [1,2,3,4,5,6,7,8,9]

                for x in sudoku[i][:]:
                    if x in temp_domain:
                        temp_domain.remove(x)
                for y in sudoku[:, j][:]:
                    if y in temp_domain:
                        temp_domain.remove(y)
                print("1")
                return i,j,temp_domain


    return None


def algor(sudoku):

    find = empty(sudoku)
    print("0")
    print(find)
    if not find:
        # count = count + 1
        # print(sudoku,"\n")
        return True
    else:
        row, col, domain = find
        # print(find)
        # forward_checking(row, col)
# this need to change to tempdomain 
    for i in domain:
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i
            if algor(sudoku):
                return True

            sudoku[row][col] = 0

    return False

# 
def valid(sudoku, det, loc):
    # Check row
    for i in range(len(sudoku[0])):
        if sudoku[loc[0]][i] == det:
            return False

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][loc[1]] == det:
            return False

    # Check box
    matrix_x = loc[1] // 3
    matrix_y = loc[0] // 3

    for i in range(matrix_y*3, matrix_y*3 + 3):
        for j in range(matrix_x * 3, matrix_x*3 + 3):
            if sudoku[i][j] == det:
                return False

    return True



print(sudoku, "\n")
print("________________________")
def sudoku_solver(sudoku):
    if algor(sudoku) == True:
        return sudoku
    else:
        return fail_board
print(sudoku_solver(sudoku))




