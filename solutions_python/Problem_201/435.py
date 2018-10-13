# David Mende
# Google Code Jam 2017
# Qualification Round
# Problem C

def stallgap(n,k):
	p = 2**(k.bit_length()-1)
	q,r = divmod(n-p+1,p)
	return q+1 if k-p < r else q

def stalldist(n,k):
	q = stallgap(n,k)
	r = q//2
	return (r,r-1) if q % 2 == 0 else (r,r)

for i in range(int(input())):
	n,k = [int(a) for a in input().split()]
	print('Case #'+str(i+1)+':',*stalldist(n,k))
