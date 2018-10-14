import sys

a = open("input.in")
b = open("output.txt","w")

#    a.readline()
#    int(a.readline())
#    map(int,a.readline().split())
#    list(map(int,a.readline().split()))

for case in xrange(int(a.readline())):
    A,B,k = map(int,a.readline().split())
    count = 0
    for i in xrange(A):
        for j in xrange(B):
            if i&j < k:
                #print a,b
                count += 1
    line = "Case #%d: %d\n"%(case+1,count)
    print line
    b.write(line)
