def xl(l):
    return xrange(len(l))

s={0:"OFF",1:"ON"}
for case in range(input()):
    print "Case #"+str(case+1)+":",
    n,k=map(int,raw_input().split())
    print s[(((k)>>n)%2) ^ (((k+1)>>n)%2)]
