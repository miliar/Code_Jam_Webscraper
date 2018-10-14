#!/usr/bin/python
import math

fp = open('d.in')

fp.readline()

c = 0

kk = 15
#prob = kk*[0]
exp = kk*[0]
exp[0] = 0.0
exp[1] = 0.0
exp[2] = 2.0
#prob[1] = 1
#prob[2] = 0.5

def derangements(n):
#	a = [1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961, 14684570, 176214841, 2290792932]
#	return a[n]
	return math.floor(math.factorial(n)/math.e + 0.5)

for i in range(3,kk-1):
#	prob[i] = 1.0/math.factorial(i)
	heldOut = derangements(i)
	heldIn = math.factorial(i)-heldOut
#	print heldIn / math.factorial(i)
	exp[i] = 1.0
	
	for j in range(1,i-1):	
		exp[i] = exp[i] + (math.factorial(i)*derangements(i-j))/(math.factorial(j)*math.factorial(i-j))/math.factorial(i) * exp[i-j]	

	exp[i] = exp[i] * math.factorial(i)/heldIn


for line in fp:
	line = line[:-1]
	if c % 2 == 1:
		arr = line.split(' ')
		arr = [int(x)-1 for x in arr]
		s = 0
		s2 = 0
		bucket = []
#		print "Started with ", arr
		for i in range(len(arr)):
			if arr[i] == i:
				continue
			else:
				cc = i
				bucket = []
				while (arr[cc] != -1):
					bucket.append(arr[cc])
					tmp = arr[cc]
					arr[cc] = -1
					cc = tmp				
				if len(bucket) > 0:
#					print bucket
#					s = s + exp[len(bucket)]
					s2 = s2 + len(bucket)
		print "Case #%d: %0.6f" % (c/2+1, s2)
#		print arr
	c = c + 1