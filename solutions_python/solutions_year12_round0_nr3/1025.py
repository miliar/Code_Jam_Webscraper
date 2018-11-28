tests=int(raw_input())
 
for t in range(1,tests+1):
        a,b=(int(x) for x in raw_input().split())
        considered={}
        ans=0
        
        for x in range(a,b+1):
                s=str(x)
                length=len(s)
                for l in range(length-1):
                        s=s[-1]+s[:length-1]
                        temp=int(s)
                        if temp>=a and temp<=b and temp!=x:
                                if min(temp,x) not in considered:
                                        ans+=1
                                        considered[min(temp,x)]=[max(temp,x)]
                                        
                                elif max(temp,x) not in considered[min(temp,x)]:
                                        ans+=1
                                        considered[min(temp,x)].append(max(temp,x))              
                
        print "Case #" + str(t) + ": " + str(ans)