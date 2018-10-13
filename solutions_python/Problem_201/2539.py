
def lar(ref):
    m=0
    (start,end)=ref[0]
    for yo in ref:
        (s,e)=yo
        if (e-s)>m:
            m=e-s
            (start,end)=(s,e)
    
    
    ref.remove((start,end))
    return (start,end)

n= input()
for i in range(n):
    (num,k) = raw_input().split()
    num=int(num)
    k=int(k)
    l=[]
    ref=[]
    pos=0
    
    for j in range(num):
        l.append(0)

    ref.append((0,num-1))
    for j in range(k):
        ls=0
        rs=0
        (start,end)=lar(ref)
        
        pos=int((end+start+1)/2)
        l[pos]=1
        if start<=pos-1:
            ref.append((start,pos-1))
        if pos+1<=end:
            ref.append((pos+1,end))
        ls=pos-start
        rs=end-pos
            
        

        

    
    
    p=max(ls,rs)
    q=min(ls,rs)
    if p<0 :
        p=0

    if q<0:
        q=0
        
    print "Case #"+str(i+1)+": "+str(p)+" "+str(q)

    









    
    
            
        
        
            
            
        
