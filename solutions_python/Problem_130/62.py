import sys

#can i possibly win?
def canwin(i,n,p):
	#to get k wins I need to be able to defeat 2^k-1 teams
	k=0
	while 2**(k+1) <= 2**n-i: k += 1
	#I can have k wins
	bestcaseranking = 2**(n-k)-1
	return bestcaseranking < p

#can i be guaranteed a win?
def guaranteedwin(i,n,p):
	k=0
	while 2**(k+1)-1 <= i: k += 1
	worstcaseranking = 2**n-2**(n-k)
	return worstcaseranking < p


#binary search
#max i s.t. f(i)
#0<=i<2^n
def bsearch(f,n):
	mini=0
	supi=2**n
	while mini+1 < supi:
		mid=(mini+supi)/2
		if f(mid):
			mini=mid
		else:
			supi=mid
	return mini

#find the range of i that must win and can win
def findrange(n,p):
	f = lambda i: guaranteedwin(i,n,p)
	imust = bsearch(f,n)
	f = lambda i: canwin(i,n,p)
	ican = bsearch(f,n)
	return imust,ican

t = int(sys.stdin.readline())
for c in range(t):
	np=sys.stdin.readline().split()
	n=int(np[0])
	p=int(np[1])
	imust,ican = findrange(n,p)
	assert canwin(ican,n,p)
	assert ican==2**n-1 or not canwin(ican+1,n,p)
	assert guaranteedwin(imust,n,p)
	assert imust==2**n-1 or not guaranteedwin(imust+1,n,p)
	print "Case #"+str(c+1)+": "+str(imust)+" "+str(ican)
