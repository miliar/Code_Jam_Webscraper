N = 500
tab = []
tab.append([1]+[0]*N)
for n in range(1, N):
	tab.append([1]+[0]*N)
	for k in range(1,n+1):
		tab[n][k] = tab[n-1][k]+tab[n-1][k-1]
pure = [[], [1]]
for n in range(2, N+1):
	pure.append([0]*n)
	for k in range(1, n):
		pure[n][k] = sum([pure[k][i]*tab[n-k-1][k-i-1] for i in range(0, k)])
print "calc"

import sys
f = sys.argv[1]
fin = open(f)
fout = open(f.replace('in','out'), 'w')
T = int(fin.next())
for k in range(0, T):
	N = int(fin.next())
	fout.write("Case #%d: %d\n"%(k+1, sum(pure[N])%100003))
