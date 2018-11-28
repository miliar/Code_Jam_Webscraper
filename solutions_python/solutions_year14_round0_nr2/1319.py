#!/usr/bin/env python

def compute(C, F, X):
    n = int((X / C) - (2.0 / F))
    if n < 1:
        return X / 2.0
    else:
        result = X / (2.0 + n*F)
        for i in range(n):
            result = result + (C / (2.0 + (i*F)))
        return result

if __name__ == "__main__":
    import sys
    from string import strip, split
    num = int(sys.stdin.readline())
    for i in range(1, num+1):
        line = split(strip(sys.stdin.readline()))
        [C, F, X] = map(lambda x:float(x), line)
        print "Case #%d: %.7f" %(i, compute(C, F, X))

