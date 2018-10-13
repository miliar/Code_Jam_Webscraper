#!/usr/bin/env python

#getting arguments
import sys
import getopt
usage = \
"""
Usage:
googlenese.py -f file.inp
"""
if len(sys.argv)<3:
    print usage
    sys.exit()

opts, args = getopt.getopt(sys.argv[1:],"f:h:")
for o,a in opts:
    if o == "-h":
        print usage
        sys.exit()
    elif o == "-f": f=a
    else: print 'Invalid Option'

#GOOGLENESE EQUIVALENCE
google = {'y':'a', 'l':'g', 'm':'l', 'z':'q', 'g':'v',
          'n':'b', 'b':'h', 'x':'m', 'p':'r', 't':'w',
          'f':'c', 'k':'i', 's':'n', 'd':'s', 'h':'x',
          'i':'d', 'u':'j', 'e':'o', 'r':'t', 'a':'y',
          'c':'e', 'o':'k', 'v':'p', 'j':'u', 'q':'z',
          'w':'f',
          'Y':'A', 'L':'G', 'M':'L', 'Z':'Q', 'G':'V',
          'N':'B', 'B':'H', 'X':'M', 'P':'R', 'T':'W',
          'F':'C', 'K':'I', 'S':'N', 'D':'S', 'H':'X',
          'I':'D', 'U':'J', 'E':'O', 'R':'T', 'A':'Y',
          'C':'E', 'O':'K', 'V':'P', 'J':'U', 'Q':'Z',
          'W':'F'}

#OPENING INPUT

lines=[]
for line in open(f):
    line=line.rstrip()
    temp=line.split()
    lines.append(temp)
del lines[0]

#CREATING OUTPUT FILE
output=open('googlenese.out','w')

#TRANSLATING
for i in range(len(lines)):
    output.write("Case #%d: "%(i+1))
    for j in range(len(lines[i])):
        for c in range(len(lines[i][j])):
            output.write("%s"%google[lines[i][j][c]])
        output.write(" ")
    output.write("\n")

