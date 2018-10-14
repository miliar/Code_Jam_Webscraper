ans=""
for i in range(int(raw_input())):
        c=0
        Smax,ar=raw_input().split()
        Smax=int(Smax)
        ar=list(ar)
        ar=map(int,ar)
        j=1
        s=ar[0]
        while j<len(ar):
             if j>s:
                     c=c+j-s
                     s=s+j-s
             s=s+ar[j]       
             j=j+1
        ans=ans+"Case #"+str(i+1)+": "+str(c)+"\n"
print ans        
