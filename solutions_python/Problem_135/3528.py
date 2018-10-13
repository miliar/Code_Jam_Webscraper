#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def get_input(filename):
    fichier = open(filename, "r")
    data = fichier.read()
    fichier.close()
    return filter(None, data.split("\n"))

lines = []    
lines = get_input(sys.argv[1])

n_test_cases = int(lines[0])

lines = lines[1:]

for i in range(n_test_cases):
    case = lines[10*i:10+10*i]
    case = [map(int, row.split()) for row in case]
    rows = []
    matrixs = [row for row in case if len(row) > 1]
    rows = []
    for j in range(2):
        matrix = matrixs[j*4:(j+1)*4]
        rows.append(matrix[case[j*5][0]-1])
    common = [a for a in rows[0] if a in rows[1]]
    if len(common) == 1:
        print "Case #%d: %d" % (i+1, common[0])
    elif len(common) == 0:
        print "Case #%d: Volunteer cheated!" % (i+1)
    else:
        print "Case #%d: Bad magician!" % (i+1)
