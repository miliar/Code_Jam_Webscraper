from operator import xor
for case in range(input()):
    raw_input()
    l=map(int,raw_input().split())
    print "Case #"+str(case+1)+":",
    if reduce(xor,l):
        print "NO"
    else:
        print sum(l)-min(l)
