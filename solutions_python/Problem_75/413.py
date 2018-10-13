from __future__ import print_function

T = int(raw_input())
for i in range(T):
    line = raw_input().split()
    C = int(line[0])
    Cn=[] # combine to give nonbase element
    for x in range(1,C+1):
        Cn+=[(line[x][:-1],line[x][-1])]
    D = int(line[C+1])
    Dn=[] #the base elements opposed to each other
    for x in range(C+2,(C+2)+(D)):
        Dn+=[line[x]]
    N=line[C+2+D]
    toInvoke=list(line[C+D+3])

    #actual code

    invoked=[]
    while len(toInvoke)!=0:
        invoked+=[toInvoke.pop(0)]
        combined=False
        for x,y in Cn:
            if(len(invoked)>=len(x) and
               sorted(x) == sorted(invoked[len(invoked)-len(x):])):
                for a in range(len(x)):
                    invoked.pop()
                invoked+=[y]
                combined=True
                break
        if(combined):
            continue
        for x in invoked[:-1]:
            if(x+invoked[-1] in Dn or invoked[-1]+x in Dn):
                invoked=[]
                break
        
    print("Case #%d: ["%(i+1),sep='',end='')
    for x in range(len(invoked)):
        print(invoked[x],sep='',end='')
        if(x!=len(invoked)-1):
            print(", ",sep='',end='')
    print("]")
    
        
            
