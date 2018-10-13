def solve(X, R, C):
    if R*C % X != 0:
        return "RICHARD"
    else:
        if min(R, C) <= X / 2 and X != 2:
            return "RICHARD"
        else:
            return "GABRIEL"

if __name__ == '__main__':
     cases = input()
     for i in range(cases):
        X, R, C = map(int, raw_input().split(" "))
        print "Case #%d: %s" % (i+1, solve(X, R, C))


