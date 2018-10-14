#!/usr/bin/python
import sys

def calc_ans(line, phrase):
    mat = []
    for x in xrange(len(line)+1):
        mat.append([])
        for y in xrange(len(phrase)+1):
            mat[-1].append(None)

    for y in xrange(len(phrase)+1):
        mat[len(line)][y] = 0

    for x in xrange(len(line)+1):
        mat[x][len(phrase)] = 1

    for x in xrange(len(line)-1, -1, -1):
        for y in xrange(len(phrase)-1, -1, -1):
            mat[x][y] = (mat[x+1][y] + mat[x+1][y+1]*(line[x] == phrase[y]))%10000

    return mat[0][0]

def main():
    phrase = "welcome to code jam"
    handle = file(sys.argv[1])
    N = int(handle.readline())
    for case_no in range(1,N+1):
        line = handle.readline()[:-1]
        print "Case #%d: %04d" % (case_no, calc_ans(line, phrase))

main()
