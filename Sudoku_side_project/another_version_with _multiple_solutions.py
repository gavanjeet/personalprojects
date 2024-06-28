# another version using numpy to print board and get mutiple solutions(uses recursion as well)

import numpy as np

board = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def possible(row, column, number):
    global board
    #Is the number appearing in the given row?
    for i in range(0,9):
        if board[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if board[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    box_x = (column // 3) * 3
    box_y = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if board[box_y+i][box_x+j] == number:
                return False

    return True

def solve():
    global board
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0

                return
      
    print(np.matrix(board))
    input('More possible solutions')

solve()