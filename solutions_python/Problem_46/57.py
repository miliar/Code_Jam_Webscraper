from sys import stdin
from sys import stdout

for x in xrange(int(stdin.readline())):
    n = int(stdin.readline())
    l = [stdin.readline().strip().rfind('1') for i in xrange(n)]
    k = 0

    for i in xrange(n):
        if l[i] > i:
            j = i + 1
            while l[j] > i: j+=1
            k += j-i
            tmp = l[j]
            l[i+1:j+1] = l[i:j]
            l[i] = tmp
    print "Case #%d: %d" % (x+1, k)