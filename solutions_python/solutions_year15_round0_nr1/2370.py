t=int(raw_input())
for i in range(t):
    smax,s=raw_input().split()
    if int(smax)==0:
        print "Case #"+str(i+1)+": "+str(0)
    else:
        available=0
        needcounter=0
        for j in range(1,len(s)):
            needed=j
            available+=int(s[j-1])
            while needed-available>0:
                needcounter+=1
                available+=1
        print "Case #"+str(i+1)+": "+str(needcounter)
