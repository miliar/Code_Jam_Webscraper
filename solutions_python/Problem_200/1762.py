
fr=open('B-large.in','r')
fw=open('out_large.txt','w')
T=int(fr.readline())
for z in range(T):
	N=str(int(fr.readline()))
	N=[int(i) for i in N]
	ans=[]
	for i in range(len(N)):
		if len(ans)==0 or N[i]>=ans[-1]: ans.append(N[i])
		else:
			while len(ans)>1 and ans[-1]-1<ans[-2]: ans.pop()
			ans[-1]-=1
			break
	ans.extend([9]*(len(N)-len(ans)))
	if ans[0]==0: ans=ans[1:]
	ans = [str(i) for i in ans]
	ans=''.join(ans)
	#print 'Case #%d: %s\n'%(z+1,ans)
	fw.write('Case #%d: %s\n'%(z+1,ans))

"""
from bisect import bisect
ans=[]
for i in range(1,1001):
	z,f=str(i),1
	for j in range(len(z)-1):
		if z[j]>z[j+1]: f=0
	if f: ans.append(int(z))
print ans
"""
"""
fr=open('B-small-attempt2.in','r')
fw=open('out_pp.txt','w')
T=int(fr.readline())
for mz in range(T):
	N=int(fr.readline())
	for i in range(N,0,-1):
		z,f=str(i),1
		for j in range(len(z)-1):
			if z[j]>z[j+1]: f=0
		if f==1: 
			ans=int(z)
			break
	fw.write('Case #%d: %s\n'%(mz+1,ans))
"""