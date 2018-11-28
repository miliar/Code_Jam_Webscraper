"""
#algo:
(1) Keep running sum.
(2) From i=0 to SMax, n = n + 1, sum = sum + 1 if sum < i + 1
"""

f = open('A-small-attempt0.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for i in range(1, T+1):
    l = f.readline()
    l = l.split(' ')
    smax = int(l[0][0])

    ppl = 0
    invites = 0
    for j in range(0, smax+1):
        ppl += int(l[1][j])
        if(ppl < j+1):
            invites+=1
            ppl += 1

    outline = "Case #%d: %d\n" % (i, invites)
    o.write(outline)

o.close()
