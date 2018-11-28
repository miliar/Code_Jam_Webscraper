#!/usr/bin/env python
import sys

def main():
    data = [line.rstrip() for line in sys.stdin]
    cases = data[0]
    for i in xrange(int(cases)):
        x = (i * 10) + 1 #case start line
        row1 = int(data[x])
        table1 = [data[x+1], data[x+2], data[x+3], data[x+4]]
        row2 = int(data[x+5])
        table2 = [data[x+6], data[x+7], data[x+8], data[x+9]]

        handleCase(i + 1, row1, table1, row2, table2)

def handleCase(case, row1, table1, row2, table2):

    #print 'case: #', case, row1, table1, row2, table2
    possible1 = table1[row1 -1].split()
    #print possible1
    possible2 = table2[row2 -1].split()
    #print possible2

    overlap = set(possible1).intersection(set(possible2))
    #print overlap

    length = len(list(overlap))

    out = ''
    if length == 1:
        out = list(overlap)[0]
    elif length == 0:
        out = 'Volunteer cheated!'
    elif length > 1:
        out = 'Bad magician!'
    else:
        out = 'SOMETHIGN"S WRONG'

    print 'Case #' + str(case) + ': ' + out

main()
