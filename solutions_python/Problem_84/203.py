#!/usr/bin/env python
import sys

def solve(matrix):
    result = []
    for i in xrange(0, len(matrix)):
        for j in xrange(0, len(matrix[i])):
            if matrix[i][j] == '#':
                try:
                    
                    if matrix[i+1][j] == '#' and matrix[i][j+1] == '#' and matrix[i+1][j+1] == '#':
                        matrix[i][j] = '/'
                        matrix[i+1][j] = '\\'
                        matrix[i][j+1] = '\\'
                        matrix[i+1][j+1] = '/'
                    else:
                        return ['Impossible']
                except IndexError:
                    return ['Impossible']
    return matrix

if __name__ == "__main__":
    infile = open('A-large.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        matrix = []
        rows = infile.readline()
        rows = int(rows[0])
        for r in xrange(0,rows):
            matrix.append([])
            matrix[r].extend(infile.readline().strip())
        result = solve(matrix)
        outfile.write(("Case #%d:\n") % int(i+1))
        for line in result:
            outfile.write(("%s\n") % ''.join(line))
    infile.close()
