file_name='C-small-attempt0.in'

from functools import reduce
def dmul(a,b):
	if a[0]=='-':
		tmp = dmul(a[1:],b)
		if tmp[0]=='-':
			return tmp[1:]
		else:
			return '-'+tmp
	if b[0]=='-':
		tmp = dmul(a,b[1:])
		if tmp[0]=='-':
			return tmp[1:]
		else:
			return '-'+tmp
	if a=='1':
		return b
	if b=='1':
		return a
	if a==b:
		return '-1'
	if a=='i':
		if b=='j':
			return 'k'
		if b=='k':
			return '-j'
	if a=='j':
		if b=='i':
			return '-k'
		if b=='k':
			return 'i'
	if a=='k':
		if b=='i':
			return 'j'
		if b=='j':
			return '-i'
def dcalc(s):
	return reduce(dmul,s)

f=open(file_name,'r')
T=eval(f.readline())
result=open('c.out','w')
for t in range(T):
	# print('testing case '+str(t+1))
	[L, X]=f.readline().split()
	L=eval(L)
	X=eval(X)
	s=f.readline()
	curr='1'
	goal='i'
	for i in range(X):
		for j in range(L):
			curr=dmul(curr,s[j])
			# print(curr)
			if goal != 'done' and curr==goal:
				# print('goal '+goal+' reached!')

				if goal=='i':

					goal='j'
					curr='1'
				elif goal=='j':
					goal='k'
					curr='1'
				elif goal=='k':
					goal='done'
					curr='1'
	if curr=='1' and goal=='done':
		# print('YES')
		result.write('Case #'+str(t+1)+': '+'YES'+'\r')
	else:
		# print('NO')
		result.write('Case #'+str(t+1)+': '+'NO'+'\r')
	
f.close()
result.close()