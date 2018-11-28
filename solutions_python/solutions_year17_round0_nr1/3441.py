t=int(raw_input().strip())
for i in range(t):
    inp=raw_input().strip().split(" ")
    s=list(inp[0])
    k=int(inp[1])
    flag=0
    for j in range(len(s)):
    	if(j==len(s)-k+1):
    		break
    	if(s[j]=='-'):
    		flag=flag+1
    		for x in range(j,j+k):
    			if(s[x]=="+"):
    				s[x]='-'
    			else:
    				s[x]='+'
    if("".join(s)=="+"*len(s)):
    	print("Case #"+str((i+1))+": "+str(flag))
    else:
    	print("Case #"+str((i+1))+": IMPOSSIBLE")
