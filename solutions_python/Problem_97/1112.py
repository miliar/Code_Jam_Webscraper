import sys


def rotate(n):
	return n[-1]+n[:-1]



oF = open(sys.argv[1])

T = int(oF.readline().strip())

for i in range(T):
	limits = [int(x) for x in oF.readline().strip().split()]
	A = limits[0]
	B = limits[1]
	count = 0
	for n in range(A,B+1):
		#hist = []
		original = str(n)
		m = rotate(original)
		#hist.append(m)
		while int(m)!=int(original):
			if int(m)>n and int(m) in range(A,B+1):# and m not in hist:
				#print m
				count=count+1
				#hist.append(m)
			m = rotate(m)


	print 'Case #'+str(i+1)+': ',count 
		
