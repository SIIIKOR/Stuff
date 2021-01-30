import numpy as np
import matplotlib.pyplot as plt
import time


def surroundings(x, y, size):
    xs = [(x+i) for i in range(-1, 2) if (x+i) >= 0 if (x+i) <= size-1]
    ys = [(y+i) for i in range(-1, 2) if (x+i) >= 0 if (x+i) <= size-1]
    return [(i, j) for i in xs for j in ys]


def change_state(input_matrix):
    m = input_matrix
    size = len(input_matrix) - 1
    for i in range(size):
        for j in range(size):
            cell_neighbor = surroundings(i, j, size)
            cell_neighbor_alive = [i for i in cell_neighbor if m[i[1]][i[0]] == 1]
            if m[i][j] == 1:
                if len(cell_neighbor_alive) < 2:
                    m[i][j] = 0
                elif len(cell_neighbor_alive) in [2, 3]:
                    m[i][j] = 1
                elif len(cell_neighbor_alive) > 3:
                    m[i][j] = 0
            else:
                if len(cell_neighbor_alive) == 3:
                    m[i][j] = 1
    return m


def run(size, t):
    matrix = np.random.randint(0, 2, size=(size, size))
    fig, ax = plt.subplots()
    for i in range(t):
        ax.cla()
        matrix = change_state(matrix)
        ax.imshow(matrix)
        plt.pause(0.01)


if __name__ == '__main__':
    time.sleep(5)
    run(100, 1000)
