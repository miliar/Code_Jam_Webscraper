# cook your dish here
t=int(input())
for k in range(1,t+1):
    ls=list(map(int,input()))
    i=len(ls)-1
    while i>0:
        if int(ls[i])<int(ls[i-1]):
            ls[i-1]=ls[i-1]-1
            ls[i:]=[9 for j in ls[i:]]
        i=i-1
    
    n=''.join(str(e) for e in ls)
    print("Case #%d: %d"%(k,int(n)))
    
'''    
if 9 in ls[i:]:
            ind=ls[i:].index(9)
            ls[i:ind]=[9 for j in ls[i:ind]]
        else:
        '''