def add(gaps, num, count):
	if num in gaps:
		gaps[num] += count
	else:
		gaps[num]  = count

T = int(input())
for testcase in range(1,T+1):
	N, k = [int(x) for x in input().split()]
	
	gaps={}
	gaps[N]=1
	maxgap=N
	countmax=1
	while k>countmax:
		if maxgap%2==1:
			add(gaps, maxgap//2, countmax*2)
		else:
			add(gaps, maxgap//2, countmax)
			add(gaps, maxgap//2-1, countmax)
		k -= countmax
		del gaps[maxgap]
		
		maxgap= max(gaps.keys())
		countmax=gaps[maxgap]
		#print(gaps)
	
	print("Case #"+ str(testcase)+ ":", maxgap//2, (maxgap-1)//2)