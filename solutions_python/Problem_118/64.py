def check(x):
	sq=str(x)
	return sq==sq[::-1]
ssp=[]
guess=[10**i for i in xrange(100/4+1)]
seen=set(guess)
for y in guess:
	s=str(y)
	for x in long(s+s[-2::-1]),long(s+s[::-1]):
		x_2=x**2
		if check(x_2):
			ssp.append(x_2)
			k=1
			while k<=y:
				y_k=y+k
				if y_k not in seen:
					guess.append(y_k)
					seen.add(y_k)
				k*=10
ssp=list(set(ssp))#be safe?
ssp.sort()
from bisect import bisect_left,bisect_right
for t in xrange(1,1+int(raw_input())):
	a,b=map(int,raw_input().split())
	print"Case #%d:"%t,bisect_right(ssp,b)-bisect_left(ssp,a)
