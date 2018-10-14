from fractions import gcd

cases = int(raw_input())
#print "Test cases: ", cases

testcase = 0
while( testcase < cases ):
    testcase+=1
    data = raw_input().split()
    n = int(data[0])
#    print data
    t = sorted([int(x) for x in data[1:]])
    T = abs(t[1]-t[0])
    for x in range(len(t)-1):
        T = gcd(T, t[x+1]-t[x])
#    print "gcd ", T
    y = (T - t[0]%T) % T
    for x in t:
        q = (T - (x)%T) % T
        if y <> q: print "BLAD"
    print "Case #"+str(testcase)+": " + str(y)

