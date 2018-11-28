#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    fin = open("A-large-0.in", "r")
    fout = open("A-large-0.out", "w")
    T = int(fin.readline())

    for t in xrange(0, T):
        tokens = fin.readline().strip().split()
        S_max = int(tokens[0])
        A = map(int, list(tokens[1]))
        answer = 0
        cum = 0
        for i in xrange(0, S_max):
            cum += A[i]
            answer += (i + 1 - cum - answer) if (i + 1 - cum - answer) > 0 \
                    else 0

        fout.write("Case #%i: %s\n" % (t+1, answer))

    fin.close()
    fout.close()

