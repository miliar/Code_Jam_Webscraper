
import sys
import numpy as np
import pandas as pd


def row_easy(lawn, rowix, colix):
    row = lawn[rowix,:]
    check = row <= lawn[rowix, colix]
    return np.all(check)

def col_easy(lawn, rowix, colix):
    col = lawn[:,colix]
    check = col <= lawn[rowix, colix]
    return np.all(check)

def process(lawn):
    rr, cc= np.meshgrid(range(lawn.shape[0]), range(lawn.shape[1]))
    rowset = rr.flatten()
    colset = cc.flatten()

    for i in xrange(len(rowset)):
        r = rowset[i]
        c = colset[i]
        rowcheck = row_easy(lawn, r, c)
        colcheck = col_easy(lawn, r, c)
        if not rowcheck and not colcheck:
            return False
    return True
    

if __name__ == '__main__':
    infile = open(sys.argv[1], 'rb')
    lines = map(lambda x: x.rstrip(), infile.readlines())

    N = int(lines[0])  # Number of cases
    lineIdx = 1
    caseNo = 1

    while (lineIdx < len(lines)):
        N, M = map(int, lines[lineIdx].rstrip().split(' ') )
        lineIdx += 1
        lawn = np.zeros((N,M))
        for i in xrange(N):
            lawn_row = np.array(map(int, lines[lineIdx].rstrip().split(' ')))
            lawn[i,:] = lawn_row
            lineIdx += 1
        case_res = process(lawn)
        if case_res: caseAnswer = 'YES'
        else: caseAnswer = 'NO'
        print 'Case #%d: %s' % (caseNo, caseAnswer)
        caseNo += 1
        


