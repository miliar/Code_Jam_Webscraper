caseNumber = input()
for k in range(0,caseNumber):
	ans=0
	ranges = (raw_input())
	start = int(ranges.split()[0])
	end = int(ranges.split()[1])
	for i in range(start,end+1):
		sq = int(i**(1/2.0))
		if(sq*sq == i):
			if(str(i)==str(int(str(i)[::-1]))):
				if(str(sq)==str(int(str(sq)[::-1]))):
					ans = ans+1			
	print("Case #"+str(k+1)+": "+str(ans))				
