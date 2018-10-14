import sys
#def digits(n):
#	l=[]
#	while (n/10 != 0):
#		l.append(n % 10)
#		n = n/10
#	l.append(n)
#	l.reverse()
#	return l

#def tidy(l):
#	if len(l) == 1:
#		return True
#	else:
#		return (l[0] <= l[1]) and tidy(l[1:])
#def isTidy(n):
#	return tidy(digits(n))

#tidy1000 =[]

#for i in range(1,1001):
#	if isTidy(i):
#		tidy1000.append(i)
#	else:
#		tidy1000.append(tidy1000[i-2])

# takes string of number and returns the biggest tidy number as a string
def check(l, i):
	index = i
	while index>0 :
		l[index] = str((int(l[index]) -1))
		if l[index] >= l[index -1]:
			break
		index -=1
	if index == 0:
		l[index] = str((int(l[index]) -1))
	return index +1 ######out of index problems to check
def backwards(l,i):
	i = check(l,i)
	for k in range(i,len(l)):
		l[k] ='9'

def tidy(s):
	l = list(str(int(s)))
	n = len(l)
	if n == 1:
		return l[0]
	else:
		needBack = False
		for i in range(n-1):
			if l[i] > l[i+1]:
				needBack = True
				break
		if needBack:
			backwards(l,i)
		s =''
		for k in l:
			s+=k
		return str(int(s))

f= open(sys.argv[1])
print f
out =open('out.txt','w')
T = int(f.readline())
for i in range(1, T+1):
	out.write('''Case #{}: {}\n'''.format(i, tidy(f.readline())))
f.close()
out.close()
