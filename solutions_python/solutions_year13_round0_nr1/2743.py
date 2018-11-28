#!/usr/bin/python
import sys, math, copy

def check(dataO, dataX):
	for i in range(4):
		if dataO[i] == ['O','O','O','O']:
			print "Case #%i: O won" % n
			return 0
	for i in range(4):
		if dataO[0][i] == 'O' and dataO[1][i] == 'O' and dataO[2][i] == 'O' and dataO[3][i] == 'O':
			print "Case #%i: O won" % n
			return 0
	if dataO[0][0] == 'O' and dataO[1][1] == 'O' and dataO[2][2] == 'O' and dataO[3][3] == 'O':
		print "Case #%i: O won" % n
		return 0
	if dataO[0][3] == 'O' and dataO[1][2] == 'O' and dataO[2][1] == 'O' and dataO[3][0] == 'O':
		print "Case #%i: O won" % n
		return 0
	for i in range(4):
		if dataX[i] == ['X','X','X','X']:
			print "Case #%i: X won" % n
			return 0
	for i in range(4):
		if dataX[0][i] == 'X' and dataX[1][i] == 'X' and dataX[2][i] == 'X' and dataX[3][i] == 'X':
			print "Case #%i: X won" % n
			return 0
	if dataX[0][0] == 'X' and dataX[1][1] == 'X' and dataX[2][2] == 'X' and dataX[3][3] == 'X':
		print "Case #%i: X won" % n
		return 0
	if dataX[3][3] == 'X' and dataX[2][2] == 'X' and dataX[1][1] == 'X' and dataX[0][0] == 'X':
		print "Case #%i: X won" % n
		return 0
	if True in map(lambda x: '.' in x, data):
		print "Case #%i: Game has not completed" % n
	else:
		print "Case #%i: Draw" % n
	return 0

fo = open(sys.argv[1],"r")
n=0
while fo.readline():
	n = n + 1
	data=[]
	dataO=[]
	dataX=[]
	try:
		data.append(list(fo.readline().split()[0]))
		data.append(list(fo.readline().split()[0]))
		data.append(list(fo.readline().split()[0]))
		data.append(list(fo.readline().split()[0]))
	except:
		exit(0)
	dataX = copy.deepcopy(data)
	dataO = copy.deepcopy(data)
	for i in range(4):
		if 'T' in data[i]:
			dataX[i] = map(lambda x:'X' if x=='T' else x, dataX[i])
			dataO[i] = map(lambda x:'O' if x=='T' else x, dataO[i])
	check(dataO,dataX)
