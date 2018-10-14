def main():
    t=int(input())
    m=0
    while m<t:
        m+=1
        b=int(input())
        c=input()
        d=[int(n) for n in c.split()]
        Index=0
        max=0
        sum1=1000001
        max1=0
        sum=0
        k=0
        for i in range(b):
            if d[i] > max1:
                max1 = d[i]
                Index = i
        k=max1
        sum1=k
                
        for p in range(2,int(max1/2)):
            d=[int(n) for n in c.split()]
            
            Index=0
            sum1=1000001
            max1=0
            sum=0
            k=0
            for i in range(b):
                if d[i] > max1:
                    max1 = d[i]
                    Index = i
            k=max1
            sum1=k

            while(max1>=3):        
                s=int(d[Index]/p)
                d[Index]=int(d[Index]-s)
                d.append(s)
                
                sum+=1
                l=p    
                p=2
                
                max1=0
                for i in range(b+sum):
                    if d[i] > max1:
                            max1 = d[i]
                            Index = i
                            
                            
                if(sum+max1)<sum1:
                    sum1=sum+max1
            p=l

        d=[int(n) for n in c.split()]
        Index=0
        max=0
        sum2=1000001
        max1=0
        sum=0
        k=0
        for i in range(b):
                if d[i] > max1:
                        max1 = d[i]
                        Index = i
        k=max1
        sum2=k
        while(max1>=3):
            s=int(d[Index]/2)
            d[Index]=int((d[Index])/2+(d[Index])%2)
            d.append(s)
            
            sum+=1
            
            max1=0
            for i in range(b+sum):
                if d[i] > max1:
                        max1 = d[i]
                        Index = i
                        
                        
            if(sum+max1)<sum2:
                sum2=sum+max1
        sum1=min(sum1,sum2)
        
        print("Case #%s: %s"%(m,sum1))

if (__name__ == "__main__"):
          main()
