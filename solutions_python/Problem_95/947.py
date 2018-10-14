#Google Code Jam 2012 Qualification Round
#Speaking in tongues

import sys

reader = open(sys.argv[1] + '.in', 'r')
writer = open(sys.argv[1] + '.out', 'w')

t = int(reader.readline())

alphabet = "abcdefghijklmnopqrstuvwxyz"
googlerese = "ynficwlbkuomxsevzpdrjgthaq"

for i in range(t):
    line = reader.readline().split()
    newline = []
    for j in range(len(line)):
        newline.append('')
        for k in line[j]: newline[j] += alphabet[googlerese.index(k)]
    writer.write('Case #%d: ' % (i+1))
    for j in range(len(newline)):
        writer.write(newline[j])
        if j != len(newline) - 1: writer.write(' ')
        else: writer.write('\n')
        
reader.close()
writer.close()
