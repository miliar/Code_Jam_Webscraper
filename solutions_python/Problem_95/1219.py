#!/usr/bin/python
import sys

def read_inp():
	N = int(inp.readline())

	lines = []
	n = N
	while n > 0:
		lines.append(inp.readline()[:-1])
		n = n - 1
	return lines

inp = sys.stdin
codedict = {' ':' ', 'a':'y', 'c':'e', 'b':'h', 'e':'o', 'd':'s', 'g':'v', 'f':'c', 'i':'d', 'h':'x', 'k':'i', 'j':'u', 'm':'l', 'l':'g', 'o':'k', 'n':'b', 'q':'z', 'p':'r', 's':'n', 'r':'t', 'u':'j', 't':'w', 'w':'f', 'v':'p', 'y':'a', 'x':'m', 'z':'q'}

lines = read_inp()
oplines = []
for line in lines:
	newopline = [codedict[ch] for ch in line]
	strtemp = "".join(newopline)
	oplines.append(strtemp)

fout = open('tout.txt','w')
for (i,line) in enumerate(oplines):
	fout.write('Case #'+str(i+1)+': '+line+'\n')
	print 'Case #'+str(i+1)+': '+line
fout.close()

	
