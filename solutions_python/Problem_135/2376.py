import sys
fpin=open('A-small-attempt0.in','r')
fpout=open('outa.txt','w')
sys.stdin=fpin
sys.stdout=fpout
T=input()
for testcase in xrange(1,T+1):
	fd={}
	firstas=input()
	ans=[[0]*4 for i in range(4)]
	for i in range(4):
		ans[i]=map(int,raw_input().split(' '))
	for x in ans[firstas-1]:
		fd[x]=1
	secondas=input()
	ans2=[[0]*4 for i in range(4)]
	for i in range(4):
		ans2[i]=map(int,raw_input().split(' '))
	cnt=0
	for x in ans2[secondas-1]:
		if fd.has_key(x):
			cnt+=1
			res=x
	if cnt==0:
		res="Volunteer cheated!"
	elif cnt>1:
		res="Bad magician!"
	print 'Case #%d:'%(testcase),res
fpin.close()
fpout.close()