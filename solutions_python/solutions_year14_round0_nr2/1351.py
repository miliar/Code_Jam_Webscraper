#!/usr/bin/env python3
import sys

def cookieClickerSolver(C, F, X):
    # my production
    P = 2.0
    # my cookie jar
    J = 0.0
    # Total time
    T = 0.0

    # is buying worth it?
    timeafter = lambda c, f, x, p: c/p + x/(p+f)
    worthit = lambda c, f, x, p: x/p > timeafter(c,f,x,p)

    
    while J < X:
        if worthit(C, F, X, P):
            # the time to be able to buy
            T += C/P
            # my new production
            P += F
        else:
            T += (X - J) / P
            J = X

    return T

def main(argv):
    if len(argv) != 2:
        print("Usage : {} input".format(argv[0]))
        return -1

    with open(argv[1]) as infile:
        nb_tests = int(infile.readline())

        #lets read the input!
        for t in range(nb_tests):
            C, F, X = [float(e) for e in infile.readline().split()]
            T = cookieClickerSolver(C, F, X)
            print("Case #{0}: {1:.7f}".format(t+1, T))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
