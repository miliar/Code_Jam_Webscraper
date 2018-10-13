import string
import sys

instr =  "abcdefghijklmnopqrstuvwxyz"
outstr = "ynficwlbkuomxsevzpdrjgthaq"

table = string.maketrans(outstr, instr)

t = input()

for i in range(t):
	s = sys.stdin.readline()
	print "Case #{0}: {1}".format(i+1,string.translate(s[:-1], table))