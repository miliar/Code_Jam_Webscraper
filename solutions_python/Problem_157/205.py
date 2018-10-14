import re
import sys
import random
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())

tr = [
	[0,0,0,0,0],
	[0,1,2,3,4],
	[0,2,-1,4,-3],
	[0,3,-4,-1,2],
	[0,4,3,-2,-1]
]

def mul(a,b):
	return (-1 if (a<0) ^ (b<0) else 1) * tr[abs(a)][abs(b)]
#def mul_state
def pow(x,k):
	b = reversed(bin(k)[2:])
	out = 1
	for sz,i in enumerate(b):
		sz = 2**(sz-1)
		if(i=='1'):
			out = mul(out,x)
		x=mul(x,x)
	return out
def get_poss(x,k):
	poss={1:0}
	cur = 1
	for i in range(k):
		cur=mul(cur,x)
		if cur in poss:
			return poss
		poss[cur] = i+1
	return poss
def get_poss_rewrite(x,k,oposs):
	poss1,poss2={1:0},{}
	cur = 1
	for i in range(k):
		cur=mul(cur,x)
		if cur in poss1:
			if cur in poss2:
				return oposs
			poss2[cur] = i+1
			oposs[cur] = i+1
		else:
			poss1[cur] = i+1
	return oposs
def find_n(poss,l,s,target,position):
	mini = -1
	cur = [[i,poss[i]] for i in poss]
	for k,i in enumerate(s):
		for j in cur:
			j[0] = mul(j[0],i)
			if(j[0] == target and (j[1],k)>position):
				if mini == -1:
					mini=(j[1],k)
				else:
					mini = min(mini,(j[1],k))
	return mini

sys.stdin = open('input.txt')
ofg=1
if ofg:
	sys.stdout = open('output.txt','w')
for t in range(scan()):
	sys.stderr.write('@%d \n'%(t+1))
	l,d = scan(),scan()
	mp = {'1':1,'i':2,'j':3,'k':4}
	s = [mp[i] for i in scans()]
	etl = 1
	for i in s:
		etl=mul(etl,i)
	if pow(etl,d)!=-1:
		print('Case #%d: NO'%(t+1)) # Not possible
		continue
	# print(get_poss(etl,d-1))
	# print()
	ret=find_n(get_poss(etl,d-1),l,s,2,(-1,0))
	if(ret==-1):
		# print('I notfound')
		print('Case #%d: NO'%(t+1)) # Not possible
		continue
	ret=find_n(get_poss_rewrite(etl,d-1,get_poss(etl,d-1)),l,s,4,ret)
	if(ret==-1):
		# print('J notfound')
		print('Case #%d: NO'%(t+1)) # Not possible
		continue
	# print('J at '+str(ret))
	print('Case #%d: YES'%(t+1))
if ofg:
	sys.stdout.flush()
	sys.stdout.close()