t = input()
for i in range(t):
    maxShy,arr = raw_input().split()
    invite = [0]
    curr = 0
    
    for j in range(int(maxShy)+1):
    	if j==0:
    		curr += int(arr[j])
    		continue
    	if int(arr[j])<1:
    		continue
    	if curr>=j:
    		curr += int(arr[j])
    	else:
    		if j-curr<=j:
    			invite.append(j-curr)
    			curr=j+int(arr[j])
    		else:
    			print "here"
    
    print "Case #"+str(i+1)+": "+str(sum(invite))
