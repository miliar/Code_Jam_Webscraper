# -*- coding:utf-8 -*-

import numpy as np
import sys

fn = "B-large.in"
infile = open(fn,'r')
outfile = open("lawn.out",'w')

case_num = int(infile.readline().strip())

def ispossible(rs):
	m, n = rs.shape
	if m == 1 and n == 1:
		return True
	try:
		mh = np.min(rs)
	except:
		return True

	for i in range(0, m):
		if np.all(rs[i,:] == mh):
			return ispossible(np.append(rs[0:i,:], rs[i+1:m,:], axis=0))

	for j in range(0, n):
		if np.all(rs[:,j] == mh):
			return ispossible(np.append(rs[:,0:j], rs[:,j+1:n], axis=1))

	return False

for i in range(0,case_num):
	m, n = map(int, infile.readline().strip().split())
	rows = [[] for j in range(0,m)]
	for j in range(0,m):
		rows[j] = map(int, infile.readline().strip().split())

	rs = np.array(rows)
	if ispossible(rs):
		outfile.write("Case #{0}: {1}\n".format(str(i+1), "YES"))
	else:
		outfile.write("Case #{0}: {1}\n".format(str(i+1), "NO"))

infile.close()
outfile.close()