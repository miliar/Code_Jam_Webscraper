import math,sys,os,time

def count(x):
	a = int(x[0])
	b = int(x[1])+1
	pairs={}
	count = 0
	length = len(str(a))
	for i in range(a,b):
		c = str(i)+str(i)
		c = c[0:-1]
		for j in range(length):
			if int(c[j:j+length]) in range(a,b):
				if int(c[j:j+length]) == i:
					continue
				if pairs.has_key((i,c[j:j+length])):
					continue
				pairs[(i,c[j:j+length])]=1
				pairs[(c[j:j+length],i)]=1
				count +=1
	return count/2

file = open(sys.argv[1],'r')

for i in range(int(file.readline())):
	print "Case #" + str(i+1) + ":\t" + str(count(file.readline().split()))

