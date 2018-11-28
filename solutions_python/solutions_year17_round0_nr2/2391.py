t=input()
tt=t
while t>0:
    a=raw_input()
    b=list(a)
    b=[int(x) for x in b]
    if len(b)==1:
        k=b[0]
    else:
        while b!=sorted(b):
            
             i=0
             while i<=len(b)-2:
                  
                 
                  if b[i]>b[i+1]:
                      b[i]=b[i]-1
                      b[i+1:]=[9]*(len(b)-i-1)
                  i=i+1
                  
    if b[0]==0:
        del(b[0])
    b=[str(x) for x in b]    
    s=''.join(b)
    s=int(s)
    print 'Case #'+str(tt-t+1)+':'+' '+str(s)
    t=t-1     
                  
                 
                
