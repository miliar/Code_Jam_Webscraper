#!/usr/bin/python
import sys
import math

def squs():
	res = []
	for i in range(1, 100):
		if i %10 == 0:
			continue
		k = (i*i) % 100
		if k not in res:
			res.append(k)
 	
	return res

tails = squs()

def isPal(num):
	if num <=0:
		return False
	if num <10:
		return True

	snum = str(num)
	snum2 = snum[::-1]
	if snum == snum2 :
		return True
	return False

def isSquarePal(num):
	#print num
	if num <0:
		return False
	if num == 0:
		return True

	k = num % 100
	if k not in tails:
		return False
	testn = int(math.pow(num, 0.5) )

	ps = testn * testn
	intv = 1
	begin = 0
	if ps > num:
		intv = -1
	elif ps < num:
		intv = 1
	else:
		# ps == num:
		if isPal(testn):
			#print "%d*%d=%d : %d "%(testn, testn, testn*testn, num)
			return True
		else:
			return False
	
	
	while True:
		testn += intv
		if isPal(testn):
			ps = testn * testn
			if ps == num:
				#print "%d*%d=%d : %d "%(testn, testn, testn*testn, num)
				return True

			if (intv == -1) and (ps < num):
				return False
			if (intv == 1) and (ps > num):
				return False
			
	return False


def treatcase(line, j):
	#print "Case #%d: %s"%(j, line)
	arr = line.split()
	if len(arr)!= 2:
		print "ERROR"
		return 
	start = int(arr[0])
	end = int(arr[1])
	if start > end :
		print "ERROR"
		return 

	res = 0
	n = start
	while n <= end:
		#print "Test ", n, type(n)
		if isPal(n):
			if isSquarePal(n):
				res += 1	
		n += 1
	print "Case #%d: %d"%(j, res)
	
def testmain():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	#print Ts
	j=0
	N=0
	M=0

	part = []
	n = 0
	while True:
		j += 1
		if(j>Ts):
			return
		line=f.readline()
		line = line.strip()
		if len(line) <=0:
			break
		treatcase(line, j)

	
if __name__ == "__main__":
	testmain()
