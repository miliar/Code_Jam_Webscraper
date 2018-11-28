import sys


def solve(X, R, C):
    if X == 1:
        return True
    elif X == 2:
        if (R * C) % 2 == 0:
            return True
    elif X == 3:
        if R * C in (6, 9, 12):
            return True
    elif X == 4:
        if R * C in (12, 16):
            return True
    return False

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(1, T + 1):
        X, R, C = map(int, sys.stdin.readline().strip().split())
        if solve(X, R, C):
            print("Case #{}: GABRIEL".format(t))
        else:
            print("Case #{}: RICHARD".format(t))

main()
