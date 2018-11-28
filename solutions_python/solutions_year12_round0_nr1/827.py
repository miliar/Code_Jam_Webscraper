f = open('A-small-attempt0.in', 'r')

go=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
T=int(f.readline())
totalOut=''
for i in range(1,T+1):
    S= f.readline()
    if (('\n') in S):
        S=S[:-1]
    out=''
    for x in S: 
        if x==' ': 
            out+=' ' 
        else: 
            out+=chr(97+go.index(x))
    totalOut+= 'Case #'+str(i)+': '+out+'\n'
totalOut=totalOut[:-1]
outD= open ('A-small-attempt0.out','w')
outD.write(totalOut)