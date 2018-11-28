import sys

def check(start,end):
	global A,vo,N
	last=0
	count=0
	for i in xrange(start,end):
		if count>=N:
			break
		if not vo.has_key(A[i]):
			count+=1
		else:
			count=0

	if count>=N:
		return True
	return False
def solve1(start,end):
	global A,res
	if end-start<N:
		return
	if dp[start][end]!=-1:
		return
	if check(start,end):
		res+=1
	# b=check(start,end,last):
	for i in xrange(start+1,end):
		solve1(start,i)
		solve1(i,end)
#	print A[start:end]
	dp[start][end]=1





dp=[]
vo={'a':1,'e':1,'i':1,'o':1,'u':1}
fpin=open('A-small-attempt0.in','r')
fpout=open('outa.txt','w')
sys.stdin=fpin
sys.stdout=fpout
T=input()
for testcase in xrange(1,T+1):
	dp=[[-1]*200 for i in range(200)]
	A,N=raw_input().split(' ')
	N=int(N)
	res=0
	solve1(0,len(A))
	print 'Case #%d:'%(testcase),res
fpin.close()
fpout.close()
