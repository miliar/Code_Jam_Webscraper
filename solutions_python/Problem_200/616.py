def tidy(n):
	l=[*map(int,str(n))]
	for i in range(len(l)-1):
		if l[i]>l[i+1]:
			idx=i
			break
	try:
		while idx>0 and l[idx]==l[idx-1]:
			idx-=1
		l[idx]-=1
		for i in range(idx+1,len(l)):
			l[i]=9
		while not l[0]:
			l.pop(0)
	finally:
		return ''.join(map(str,l))

print(tidy(10))

f=open('B-large.in','r')
g=open('B-large.out','w')
for i in range(1,int(f.readline().strip())+1):
	print('Case #{}: {}'.format(i,tidy(int(f.readline()))),file=g)