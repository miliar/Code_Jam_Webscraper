def gcd(a,b):
    if b==0:
        return a
    if b>a:
        temp=b
        b=a
        a=temp
    return gcd(b,a-b)
incoming=open('A-large.in')
output=open('A-largeoutput.txt','w')
T=int(incoming.readline())
for i in range(1,T+1):
    s=incoming.readline().split()
    N=int(s[0])
    PD=int(s[1])
    PG=int(s[2])

    gc=gcd(100,PD)
    if PD==0:
        todaywinmin=0
        todayplaymin=1
    else:
       todaywinmin=PD//gc
       todayplaymin=100//gc
       
    if PD <100 and PG ==100:
        output.write("Case #%d: Broken\n"%i)
    elif todayplaymin > N:
        output.write("Case #%d: Broken\n"%i)
    elif PD>0 and PG ==0:
        output.write("Case #%d: Broken\n"%i)
    else:
        output.write("Case #%d: Possible\n"%i)
incoming.close()
output.close()
        

    
