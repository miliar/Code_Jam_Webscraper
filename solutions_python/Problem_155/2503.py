d={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

t=int(input())
for i in range(t):
	s,l=input().split()
	f=0
	s=d[l[0]]
	for j in range(1,len(l)):
		if l[j]!='0':
			if s >= j:
				s += d[l[j]]
			else:
				f += j - s
				s += j - s + d[l[j]]
	print("Case #", str(i+1), ": ", f, sep='')