"""
4
4 11111
1 09
5 110011
0 1
"""
import sys

##### Variables

##### Functions

##### Main
filename = sys.argv[1]
f = open(filename, 'r')

T = int(f.readline())
for t in xrange(T):
    (Smax, Scounts) = f.readline().split()
    Smax = int(Smax)

    cnt_all = 0
    cnt_needed = 0
    for i in xrange(len(Scounts)):

        #print (i, cnt_all)
        if cnt_all >= i:
            cnt_all += int(Scounts[i])
            continue

        cnt_needed += i - cnt_all
        cnt_all = i + int(Scounts[i])

    print 'Case #%d: %d' % (t+1, cnt_needed)

f.close()
