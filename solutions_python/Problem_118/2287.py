#!usr/bin/python
import math

filein = open("input.txt","r")
fileout = open("output.txt","w")

ffile = formater(filein)
c=0
for i in ffile:
	c=c+1
	fileout.write("Case #"+str(c)+": "+str(fairnumbers(i[0],i[1]))+"\n")
	print(fairnumbers(i[0],i[1]))
fileout.close()


def formater(filein):
	ffile = []
	intervals = []
	for line in filein:
		ffile.append(line.strip())
	ffile.remove(ffile[0])
	print(ffile)
	for i in ffile:
		t = (int(i.split()[0]),int(i.split()[1])) 
		intervals.append(t)
	print(intervals)
	return intervals


def is_palindrom(n):
	for i in range(len(str(n))//2):
		if str(n)[i]!=str(n)[-1-i]:
			return False
	return True

def is_square_palindrom(n):
	if math.sqrt(n)-math.floor(math.sqrt(n))==0:
		return is_palindrom(int(math.floor(math.sqrt(n))))


def is_fair(n):
	if  is_palindrom(n) and is_square_palindrom(n):
		return True 
	return False

def fairnumbers(a,b):
	ret = []
	for i in range(a,b+1):
		if is_fair(i):
			ret.append(i)
	return len(ret)
