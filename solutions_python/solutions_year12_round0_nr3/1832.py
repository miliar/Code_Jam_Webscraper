#!/usr/bin/python

f1 = 'C-small-attempt0.in'
f2 = 'output_RN.dat'
fin = open(f1,'r')
fout = open(f2,'w')
f = open('try.dat','w')

n = int(fin.readline())	

for i in range(n):
	string = 'Case #'+str(i+1)+':'
	a,b = [int(x) for x in fin.readline().split()]
	array = range(a,b+1)
	count = 0
	j=0
	while j<len(array):
		k = 1
		while (array[j]/(10**k))!=0:
			div = 10**k
			test = int(str(array[j]%div)+str(array[j]/div))
			if array.count(test)!=0 and test!=array[j]:
				count+=1
				print >>f, array[j],test
				#array.remove(test)
			k+=1
		j+=1
	print >>fout,string,count/2

fin.close()
fout.close()
			

