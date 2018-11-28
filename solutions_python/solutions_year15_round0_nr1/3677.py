for _ in range(int(input())):
    s=input().split()
    smax=int(s[0])
    sum,count=0,0
    audience=[int(x) for x in s[1]]
    for a in range(smax+1):
        if sum<a:
            count+=1
       	    sum+=1
	sum+=audience[a]	
    print ("Case #{}: {}".format(_+1,count))		
