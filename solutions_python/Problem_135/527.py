#!/usr/bin/env python

import sys


def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        ans1 = int(sys.stdin.readline().strip())
        mat1 = []
        for i in range(4):
            mat1.append(set(sys.stdin.readline().strip().split()))
        ans2 = int(sys.stdin.readline().strip())
        mat2 = []
        for i in range(4):
            mat2.append(set(sys.stdin.readline().strip().split()))
        inter = mat1[ans1-1].intersection(mat2[ans2-1])
        if len(inter) == 0:
            print "Case #" + str(t) + ": Volunteer cheated!"
        elif len(inter) > 1:
            print "Case #" + str(t) + ": Bad magician!"
        else:
            print "Case #" + str(t) + ": " + str(list(inter)[0])


if __name__ == '__main__':
    main()
