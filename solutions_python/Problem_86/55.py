import sys
t=int(raw_input())
for nn in range(t):
	n,l,h=map(int,raw_input().split())
	nums=map(int,raw_input().split())
	done=False
	for i in range(l,h+1):
		ok=True
		for j in range(n):
			if i>nums[j]:
				if i%nums[j]!=0:
					ok=False
			else:
				if nums[j]%i!=0:
					ok=False
		if ok :
			sys.stdout.write("Case #%d: %d\n"%(nn+1,i))
			done=True
			break
	if not done:
		sys.stdout.write("Case #%d: NO\n"%(nn+1))


		
