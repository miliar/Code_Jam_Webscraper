for c in range(int(raw_input())):
    l,k=raw_input().split()
    l=[1 if i=="+" else 0 for i in l]
    k=int(k)
    end=[0]*(len(l)+1)
    cul=0;cur=0
    for i,j in enumerate(l):
    	cur-=end[i]
    	if (j+cur)%2==0:
    		cul+=1
    		cur+=1
    		if i+k>=len(end):
    			print "Case #{}: IMPOSSIBLE".format(str(c+1))
    			break
    		else:
    			end[i+k]=1
    else:
    	print "Case #{}: {}".format(str(c+1),str(cul))