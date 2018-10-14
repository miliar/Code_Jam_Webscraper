import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r') as f:
 T = int(f.readline().strip())
 for i in range(0,T):
	 a,b = f.readline().strip().split(' ')
	 count = 0
	 extra = 0
	 for j in range(0,int(a)+1):
		 if(j >= 1):
			 if(count < j):
				 count = count+1
				 extra = extra + 1
		 count = count + int(b[j]);
	 ans = str('Case #'+str(i+1)+': '+str(extra))
	 print(ans)
