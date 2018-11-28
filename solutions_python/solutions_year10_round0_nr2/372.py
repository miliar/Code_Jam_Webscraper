def read():
    return map(int,raw_input().split()[1:])


def gcd(a,b):
    return a if b==0 else gcd(b,a%b)


def work(cases,vList):
    cycle = abs(vList[0]-vList[1])
    for i in range(len(vList)):
        for j in range(i+1,len(vList)):
            cycle = gcd(cycle,abs(vList[i]-vList[j]))

    ans = 0 if vList[0]%cycle==0 else cycle-vList[0]%cycle
    print "Case #%d: %d"%(cases,ans)
    

for i in range(int(raw_input())):
    work(i+1,read())
