t = int(raw_input())

for i in xrange(1,t+1):
    r,k,n = [long(x) for x in raw_input().split()]
    arr = [long(x) for x in raw_input().split()]
    if (sum(arr)<=k):
        print "Case #%d: %d"%(i,sum(arr)*r)
    else:
        index =[-1 for x in xrange(0,n)]
        h=0
        count=[]
        for j in xrange(0,n+1):
            if index[h] == -1: 
                index[h] = j
                p=arr[h]
                while p<=k:
                    h=(h+1)%n
                    p+=arr[h]
                count.append(p-arr[h])
            else:
                count.append(count[index[h]])
                A=index[h]+1;
                B=j-index[h];
                if (B==0):
                    B=n
                y=(r-A)%B
                x=(r-A-y)/B                
                t0=sum(count[0:A])
                t1=sum(count[A:A+B])                        
                t2=sum(count[A:A+y])
                print "Case #%d: %d"%(i,t0+t1*x+t2)
                break
