def war(a,b): 
	
	A = sorted(a)
	B = sorted(b)
	#print A
	#print B
	score = 0
	a = 0
	b = 0
	while b < len(B):
		if A[a] < B[b]:
			a = a + 1
			b = b + 1
		else:
			score = score + 1
			b = b + 1
		
	return score
	
def dwar(a,b): 
	
	A = sorted(a)
	B = sorted(b)
	#print A
	#print B
	score = 0
	a = 0
	b = 0
	while a < len(A):
		if A[a] < B[b]:
			a = a + 1
		else:
			score = score + 1
			a = a + 1
			b = b + 1
		
	return score	
	 	 
a = [.5,.1,.9]
b = [.6,.4,.3]	


f = open('D-large.in', 'r')
l = f.readline()
l = f.readline()
x = 0
c = 0
while(l):
	#print l
	if x % 3 == 1:
		a = l.split(" ")
	if x % 3 == 2:
		b = l.split(" ")
		c = c +1
		print "Case #" + str(c) + ": " + str(dwar(a,b)) + " " + str(war(a,b))
	l = f.readline()
	x = x + 1 

'''

a=[0.186,0.389,0.907,0.832,0.959,0.557,0.300,0.992,0.899]
b=[0.916,0.728,0.271,0.520,0.700,0.521,0.215,0.341,0.458]

print dwar(a,b)
print war(a,b)
'''
