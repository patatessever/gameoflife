"""
Created by @patatessever
e-mail: yunus.erzurumlu@metu.edu.tr
I dont have idea about licenses
"""

import random
import time


def dead_state(board_width, board_height):
    #Creates a board full of zeros (death cells)
    board = []
    for i in range(board_width):
        temp = []
        for j in range(board_height):
            temp.append(0)
        board.append(temp)
    return board

def random_state(board_width, board_height):
    #Creates a board with random number of alive cells
    state = dead_state(board_width, board_height)
    for i in range(board_width):
        for j in range(board_height):
            state[i][j] = random.randint(0,1)
    return state

def render(board_state):
    print("")
    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                print("#", end = " ")
            else:
                print("-", end = " ")
        print("")
    print("")

def next_cell_value(cell_coords, state):
    width = len(state)
    height = len(state[0])
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    for x1 in range((x-1), (x+1)+1):
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            if y1 < 0 or y1 >= height: continue
            if x1 == x and y1 == y: continue

            if state[x1][y1] == 1:
                n_live_neighbors += 1

    if state[x][y] == 1:
        if n_live_neighbors <= 1:
            return 0
        elif n_live_neighbors <= 3:
            return 1
        else:
            return 0
    else:
        if n_live_neighbors == 3:
            return 1
        else:
            return 0

def next_board_state(init_state):

    width = len(init_state)
    height = len(init_state[0])
    next_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), init_state)

    return next_state



def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.04)

if __name__ == "__main__":
    init_state = random_state(50, 102)
    # init_state = load_board_state('./toad.txt')
    run_forever(init_state)