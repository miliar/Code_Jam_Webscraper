import sys, math

FSs = []
MAX = 10000000

for i in range(1,MAX+1):
    s = str(i)
    if s == s[::-1]:
        j = i*i
        s = str(j)
        if s == s[::-1]:
            FSs.append(j)

#import pprint
#pprint.pprint(FSs)

lines = open(sys.argv[1],'rb').readlines()
N = int(lines[0])
for (i,l ) in enumerate(lines[1:]):
    a, b = map(int, l.split())
    count = len([n for n in FSs if (n>=a and n<=b)])
    print 'Case #%d: %d' % (i+1, count)
