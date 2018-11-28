import sys

f  = open('/home/alex/workspace/gcj_qual/A-large.in')
fo = open('/home/alex/workspace/gcj_qual/aout.txt', 'wb')
T = int(f.readline())
for t in range(T):
    l = f.readline()
    smax, s = l.strip().split(' ')
    ssum = 0
    i = 0
    ans = 0
    for d in s:
        if int(d) > 0 and ssum < i:
            ans += (i - ssum)
            ssum = i
        ssum += int(d)
        i += 1
    print "Case #%d: %d" % (t+1, ans)
    fo.write("Case #%d: %d\n" % (t+1, ans))
fo.close()
f.close()
    