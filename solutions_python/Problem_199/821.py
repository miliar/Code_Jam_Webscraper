import math
import sys

def all_happy_side(pancake_row):
    return all([pancake == '+' for pancake in pancake_row])

def flip_pancake(pancake):
    if pancake == '+':
        return '-'
    return '+'

def pancake_flips(pancake_row, k):
    if len(pancake_row) == k:
        if pancake_row[0] == '-':
            for i in range(k):
                pancake_row[i] = flip_pancake(pancake_row[i])
            if not all_happy_side(pancake_row):
                return -math.inf
            return 1
        else:
            if not all_happy_side(pancake_row):
                return -math.inf
            return 0
    if pancake_row[0] == '-':
        for i in range(k):
            pancake_row[i] = flip_pancake(pancake_row[i])
        return pancake_flips(pancake_row[1:], k) + 1
    return pancake_flips(pancake_row[1:], k)
    
    

def main():
    T = int(input())
    for i in range(1, T + 1):
        line, str_k = input().split(' ')
        pancake_row = [pancake for pancake in line]
        flips = pancake_flips(pancake_row, int(str_k))
        print("Case #{}: {}".format(i, flips if flips > -1 else "IMPOSSIBLE"))
        


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    main()
