import math

def result():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": ")
	g.write(str(count))
	g.write("\n")

def palindrome(t):
	n = str(t)
	return n==n[::-1]

def test(n):
	if palindrome(n):
		n = pow(n,2)
		if n>=start and n<=end:
			if palindrome(n):	
				return True
	return False

# open input and output files
f = open('input','r')
g = open('output','w')

# for i 0...(N-1)
for i in xrange(long(f.readline())):
	count = 0
	limits = f.readline().strip().split()
	start = long(limits[0])
	end = long(limits[1])+1
	for j in xrange(long(math.sqrt(start)),long(math.ceil(math.sqrt(end)))):
		if test(j):
			count+=1
	result()	

f.close()
g.close()

