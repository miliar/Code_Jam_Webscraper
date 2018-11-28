def solve(X, R, C):
    ans = solve_(X, R, C)
    return "GABRIEL" if ans else "RICHARD"

def solve_(X, R, C):
    if X == 1:
        return True
    if X == 2:
        return R % 2 == 0 or C % 2 == 0
    if X == 3:
        return (R, C) in ((2, 3), (3, 2), (3, 3), (3, 4), (4, 3))
    if X == 4:
        return (R, C) in ((3, 4), (4, 3), (4, 4))
    return False

if __name__ == '__main__':
    T = int(input())
    for case in range(1, T+1):
        X, R, C = (int(i) for i in input().split())
        print("Case #%d: %s" % (case, solve(X, R, C)))

