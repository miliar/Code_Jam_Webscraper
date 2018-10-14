#!/usr/bin/env python

"""
Nate Michalov
Code Jam Round 1
"""

cyph_dict = {}
eng_alph  = list('abcdefghijklmnopqrstuvwxyz')
goog_alph = list('ynficwlbkuomxsevzpdrjgthaq')

for i in range(26):
    cyph_dict[goog_alph[i]] = eng_alph[i]

def decode_lines(test_file):
    case = 0
    infile = open(test_file, 'r')
    outfile = open('output.txt', 'a')
    for line in infile:
        if len(line) > 5:
            case +=1
            outline = 'Case #'+str(case)+': '
            for i in range(len(line)):
                if line[i] not in goog_alph:
                    outline = outline+line[i]
                else:
                    outline = outline+cyph_dict[line[i]]
            outfile.write(outline)
    infile.close()
    outfile.close()

decode_lines('A-small-attempt0.in')

