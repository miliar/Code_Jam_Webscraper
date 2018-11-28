import sys

def repeated(int_a,int_b):
	n1 = str(int_a)
	i=0
	while(i<len(n1)):
		p1 = n1[0:i]
		p2 = n1[i:]
		num = int(p2+p1)
		if num==int_b:
			return True
		i=i+1
	return False

def iter(a,b):
	r=0
	for i in range(a,b+1):
		for j in range(i+1,b+1):
			s1 = str(i)
			s2 = str(j)
			if len(s1)==len(s2):
				if repeated(i,j):
					r=r+1
	return r;
		

f = file(sys.argv[1],'r');
line = f.readline()
count = int(line)
i=0;
while(i<count):
	line = f.readline()
	num = line.split(' ')
	r = iter(int(num[0]),int(num[1]))
	print "Case #%d: %d"%(i+1,r)
	i=i+1

