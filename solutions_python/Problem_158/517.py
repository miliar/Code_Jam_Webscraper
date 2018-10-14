#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    fin = open("D-small-0.in", "r")
    fout = open("D-small-0.out", "w")
    T = int(fin.readline())

    for t in xrange(0, T):
        X, R, C = tuple(map(int, fin.readline().strip().split()))

        if X == 1:
            answer = "GABRIEL"
        elif X == 2:
            answer = "RICHARD" if (R%2)*(C%2) else "GABRIEL"
        elif X == 3:
            if (R%3)*(C%3) > 0 or R*C == 3:
                answer = "RICHARD"
            else:
                answer = "GABRIEL"
        else:
            if (R*C)%4 or R*C == 4 or R*C == 8:
                answer = "RICHARD"
            else:
                answer = "GABRIEL"

        fout.write("Case #%i: %s\n" % (t+1, answer))

    fin.close()
    fout.close()

