import sys
def process(case,m,n) :	
	count = 0
	for i in range(m,n+1) :
		if square(i) and fair(i):
			if fair(int(i**0.5)) :				
				count += 1			
	print "Case #{}: {}".format(case+1,count)
# def check(num) :
# 	if square(num) and fair(num):	
# 		check
def fair(num) :
	word = str(num)
	n = len(word)
	stat = True
	if n > 1 :
		for i in range(n/2) :
			if word[i] != word[n-i-1] :
				stat = False
	return stat
def square(num) :
	tmp = num**0.5
	return tmp == int(tmp)
f = open(sys.argv[1])
n = int(f.readline())
for i in range(n) :
	
	m,n = [int(x) for x in f.readline().split()]
	process(i,m,n)
