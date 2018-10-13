f = open('ST.in', 'r')
T=int(f.readline())
totalOut=''
for i in range(1,T+1):
    S= f.readline()
    if (('\n') in S):
        S=S[:-1]
    A,B=S.split(' ')
    a=int(A)
    b=int(B)
   
    pairs=0
    for x in range(a,b): 
        found=[]
        n=m=str(x)
        lnth= len(n)
        for u in range (1,lnth):
            m=m[1:]+m[0]
            mm=int(m)
            
            if mm>x and mm<=b and not mm in found :
                pairs+=1   
                found.append(mm)
                
    totalOut+= 'Case #'+str(i)+': '+str(pairs)+'\n'
totalOut=totalOut[:-1]
outD= open ('ST.out','w')
outD.write(totalOut)