### import numpy as np
import time
from pprint import pprint as pprint
t = input()

def expand_down(cake, r, c):
    if r + 2 > len(cake):
        return cake
    else: 
        if cake[r + 1][c] == "?":
            cake[r + 1][c] = cake[r][c]
            expand_down(cake, r + 1, c)
        return cake
    
def expand_up(cake, r, c):
    if r == -1 or r == 0:
        return cake
    else: 
        if cake[r - 1][c] == "?":
            cake[r - 1][c] = cake[r][c]
            expand_up(cake, r - 1, c)
        return cake

def expand_col_left(cake, c):
    cake[:][c-1] = cake[:][c]
    

# def expand_up():
    
# def expand_left():
    
# def expand_right():

for i in range(0, int(t)):
    n = input()
    n_r = int(n.partition(' ')[0])
    n_c = int(n.partition(' ')[2])
#     cake = np.matrix
    cake = list()
    for j in range(0, n_r):
        row = input()
        row = list(row)
        cake.append(row)

    for row in range(0, n_r):
        for col in range(0, n_c):
            if cake[row][col] != "?":
                cake = expand_down(cake, row, col)
                cake = expand_up(cake, row, col)
#             for prow in range(0, n_r):
#                 print(''.join(cake[prow]))
#             time.sleep(1)
#     pprint(cake)
    while "?" in cake[0]:
        for col in range(0, n_c):
            if cake[0][col] == "?":
                if col != n_c - 1 and cake[0][col + 1] != "?":
                    for row in range(0, n_r):
                        cake[row][col] = cake[row][col + 1]
                elif col != 0 and cake[0][col - 1] != "?":
                    for row in range(0, n_r):
                        cake[row][col] = cake[row][col - 1]
#     if cake[0][-1] == "?":
#         for row in range(0, n_r):
#             cake[row][-1] = cake[row][-2]
    print("Case #" + str(i + 1) + ":")
    for row in range(0, n_r):
        print(''.join(cake[row]))
            

