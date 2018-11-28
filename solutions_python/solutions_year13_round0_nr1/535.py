#!/usr/bin/python3

T = int(input())

for t in range(T):
    grid = [list(input()) for line in range(4)]
    input()
    for line in [[grid[i][j] for j in range(4)] for i in range(4)] + \
                [[grid[j][i] for j in range(4)] for i in range(4)] + \
                [[grid[i][i] for i in range(4)]] + \
                [[grid[i][3-i] for i in range(4)]]:
        if line.count("X") == 4 or (line.count("X") == 3 and "T" in line):
            print("Case #{}: X won".format(t + 1))
            break
        elif line.count("O") == 4 or (line.count("O") == 3 and "T" in line):
            print("Case #{}: O won".format(t + 1))
            break
    else:
        if any(["." in line for line in grid]):
            print("Case #{}: Game has not completed".format(t + 1))
        else:
            print("Case #{}: Draw".format(t + 1))
