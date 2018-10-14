import logging
#logging.basicConfig(level = logging.DEBUG)

# Read input data.
import sys

args = sys.argv[1:]

# Open the file for read only.
infile = file(args[0], 'r')
lines = []
for line in infile:
    lines.append(line.strip())
infile.close()

first_line = lines.pop(0).split()
L = int(first_line[0])
D = int(first_line[1])
N = int(first_line[2])
Words = []
for n in range(D):
    Words.append(lines.pop(0))
Case = {}
for n in range(N):
    Case[n] = lines.pop(0)

for n in range(D):
    logging.debug("W:" + Words[n])

for n in range(N):
    logging.debug("C:" + Case[n])

import re

def count(words, case):
    case = case.replace('(', '[')
    case = case.replace(')', ']')
    match = re.findall(case, words)
    return len(match)

all_words = " ".join(Words)
logging.debug(all_words)
outs = []
for n in range(N):
    out = count(all_words, Case[n])
    outs.append(out)

# Printing results (Case #1: ...)
for i, out in enumerate(outs):
    print "%(c)s%(n)s: %(o)s" % {'c':"Case #", 'n':str(i+1), 'o':out}
