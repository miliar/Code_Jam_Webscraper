r=open("C:\Users\SJ\Downloads\C-small1.in",'r')

out=[]
def movedigit(s):
    return s[1:len(s)]+s[0]
def run(s):
    s=s.strip().split()
    print s
    a=int(s[0])
    b=int(s[1])
    keep={}
    count=0
    for i in range(a,b+1):
        z=str(i)
        c=1
        l=len(z)
        while(c<l):
            z=movedigit(z)
            x=int(z)
            if x>=a and x<=b and x!=i:
                if not(keep.has_key(z+' '+str(i))) and not(keep.has_key(str(i)+' '+z)):
                    keep[str(i)+' '+z]=1
                    count=count+1
            c=c+1
    print keep
    return count
def write():
    w=open("C:\Users\SJ\Downloads\Cj3.out",'w')
    for i in out:
        w.write(i)
case=r.readline()
for i in range(1,int(case)+1):
    temp=r.readline()
    out.append("Case #"+str(i)+": "+str(run(temp))+"\n")


        
    


    
                
            
        
        
        
    


    
    
    
    
    
    
    
