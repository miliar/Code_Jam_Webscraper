from numpy import array,zeros,where,nonzero,count_nonzero
from math import floor, ceil, sqrt
	
def isPalindrome(x):
	st = str(x)
	l = len(st)
	for i in xrange(0,int(floor(l/2))):
		if st[i]!=st[l-i-1]:
			return False
	return True
	
def isOddDigit(x):
	stx=str(x)
	lenx = len(stx)
	if lenx%2==0:
		return False
	else:
		return True
	
def findPalindromebetween(x,y):
	#odd digit or even digit
	stx=str(x)
	lenx = len(stx)
	odd = lenx%2
	list =[]
	nextproduct=0
	start=0
	if odd==1:
		start=stx[:(lenx/2)+1]
		tail = (start[::-1])[1:]
		nextproduct = start + tail
		if int(nextproduct)<x:
			add1=int(start)+1
			start=str(add1)
			tail = (start[::-1])[1:]
			nextproduct = start + tail
	else:
		start=stx[:(lenx/2)]
		tail = (start[::-1])
		nextproduct = start + tail
		if int(nextproduct)<x:
			add1=int(start)+1
			start=str(add1)
			tail = (start[::-1])
			nextproduct = start + tail
	
	notran=False
	while int(nextproduct)<=y:
		if odd==1:
			add1=str(int(start)+1)
			if (len(add1)!=len(start)) and (not notran):
				#print "there" + add1 + " " + start
				odd=0
				notran=True
			else:
				list.append(nextproduct)
				start=add1
				tail = (start[::-1])[1:]
				nextproduct = start + tail
				notran=False
		if odd==0:
			add1=str(int(start)+1)
			if (len(add1)!=len(start))and (not notran):
				#print "here"+ add1 + " " + start
				odd=1
				notran=True				
			else:
				if notran:
					add1=add1[:-1]
				list.append(nextproduct)
				start=add1
				tail = (start[::-1])
				nextproduct = start + tail
				notran=False
	return list
	
if __name__ == '__main__':

	f = open('C-large-1.in', 'r')
	num_samples = int(f.readline())

	for i in range(num_samples):
		dim = f.readline().split()
		min = int(dim[0])
		max = int(dim[1])
		
		a=int(ceil(sqrt(min)))
		b=int(floor(sqrt(max)))
		
		palindromebetweenab=findPalindromebetween(a,b)
		count =0 
		for p in palindromebetweenab:
			sq = int(p)**2
			if isPalindrome(sq):
				count+=1
		print "Case #" + str(i+1) + ": "+  str(count)
