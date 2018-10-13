#!/usr/bin/env python

import sys



if __name__ == "__main__":

    f = open("C-small-attempt0.in", 'r')
    fout = open("output", "w")

    T = int(f.readline())       # T test cases

    for t in xrange(T):
        line = f.readline().replace('\n', '').split(' ')
        output = "Case #" + str(t+1) + ": "
        A = int(line[0])
        B = int(line[1])
        result = 0

        for n in xrange(A, B):  # A <= n < B
            for m in xrange(n+1, B+1): #
                digits_n = [int(i) for i in str(n)]
                digits_m = [int(i) for i in str(m)]

                count = len(digits_n)
                while count > 1:
                    digits_m.insert(0, digits_m.pop()) # shift a digit
                    if digits_m == digits_n:
                        result += 1
                        break
                    count -= 1
        output = output + str(result) + '\n'
        fout.write(output)

