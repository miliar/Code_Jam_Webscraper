#!/usr/bin/python3
import sys

def prin(s):
	print(s, end="")

def nextline():
	return inf.readline().strip()

if len(sys.argv) != 2:
	sys.exit("Usage: "+sys.argv[0]+" inputfilename")
	
infilename=sys.argv[1]
inf=open(infilename,'r')

T=int(nextline())
for case in range(0,T):
	prin("Case #" + str(case+1) + ": ")
#	print()
	line=nextline()
	nos=line.split(' ')
	C=float(nos[0])
	F=float(nos[1])
	X=float(nos[2])
#	print("C={:.7f} F={:.7f} X={:.7f}".format(C, F, X))
	rate=2.0
	t=0.0
	cur=0.0
	iter=0
	while True:
		iter+=1
#		if iter > 15:
#			break
#		print('t={}, cur={}, rate={}'.format(t, cur, rate))
		if (X-cur) < C:
			t += ((X-cur)/rate)
			break
		else:
			t += (C/rate)
			cur += C
		tFarm = C / F
		tCurRate = (X-cur) / rate
		if tFarm < tCurRate:
			cur -= C
			rate += F
	print('{:.7f}'.format(t))
inf.close()
