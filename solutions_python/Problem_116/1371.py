#!/bin/python
from __future__ import print_function, division
import numpy as np
import sys


n = int(sys.stdin.readline())

def win(seq, sym):
	return all(s==sym for s in seq) or any(all(s=='T' if i==j else s==sym for (j,s) in enumerate(seq)) for i in range(4))


for case in range(n):
	rows = [sys.stdin.readline()[:4] for k in range(5)][:4]
	cols = [''.join([rows[j][i] for j in range(4)]) for i in range(4)]
	diags = [''.join(rows[i][i] for i in range(4)), ''.join(rows[i][3-i] for i in range(4))]
	seqs = rows+cols+diags

	if any(win(s,'X') for s in seqs):
		res = 'X won'
	elif any(win(s,'O') for s in seqs):
		res = 'O won'
	elif all(s != '.' for row in rows for s in row):
		res = 'Draw'
	else:
		res = 'Game has not completed'

	print('Case #%d: %s'%(case+1,res))
