import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input

def solve0(cnts):
	#roygbv
	#012345
	cnt=list(cnts)
	n=sum(cnts)
	arr=[-1]*n
	i=0
	for a in (0,2,4):
		b=(a+3)%6
		has=cnt[b]
		while cnt[b]:
			if cnt[a]:
				arr[i]=a
				cnt[a]-=1
				i+=1
			arr[i]=b
			cnt[b]-=1
			i+=1
		if has and cnt[a]:
			arr[i]=a
			cnt[a]-=1
			i+=1
	if i==0:
		for j in range(6):
			if cnt[j]:
				arr[0]=j
				cnt[j]-=1
				i=1
				break
	while i<n:
		a=arr[i-1]
		p=None
		if a==0:
			p=2 if cnt[2]>cnt[4] else 4
		if a==2:
			p=0 if cnt[0]>=cnt[4] else 4
		if a==4:
			p=0 if cnt[0]>=cnt[2] else 2
		if p==None or cnt[p]==0:
			return "IMPOSSIBLE"
		arr[i]=p
		cnt[p]-=1
		i+=1
	def cmap(i):
		return ("R","O","Y","G","B","V")[i]
	mask=(1,3,2,6,4,5)
	for i in range(n):
		j=(i+1)%n
		if mask[arr[i]]&mask[arr[j]]:
			return "IMPOSSIBLE"
	return "".join(map(cmap,arr))

cases=int(input().strip())
for cs in range(1,cases+1):
	cnts=tuple(map(int,input().strip().split()))[1:]
	print("Case #"+str(cs)+": "+str(solve0(cnts)))
