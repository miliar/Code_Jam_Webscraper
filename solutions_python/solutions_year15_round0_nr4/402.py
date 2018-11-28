import sys

def solve(fin):
    x, r, c = map(int, fin.readline().split())
    if x == 1:
        return "GABRIEL"
    if x == 2:
        if (r * c) % 2 != 0:
            return "RICHARD"
        return "GABRIEL"
    if x == 3:
        if (r * c) % 3 != 0 or min(r, c) < 2 or max(r, c) < 3:
            return "RICHARD"
        return "GABRIEL"
    if x == 4:
        if (r * c) % 4 != 0 or min(r, c) < 2 or max(r, c) < 4 or (min(r, c) == 2 and max(r, c) == 4):
            return "RICHARD"
        return "GABRIEL"

def main():
    fin = open("input.txt", "r")
    T = int(fin.readline())
    for _T in range(1, T + 1):
        print("Case #", _T, ": ", sep = "", end = "")
        print(solve(fin))
    fin.close()

main()