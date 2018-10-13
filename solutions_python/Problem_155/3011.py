inf = open('A-large.in')
outf = open('A-large.out', 'w+')
n = int(inf.readline())
#n = int(raw_input())
for i in xrange(n):
    (maxi, aud) = inf.readline().split(' ')
    people = int(aud[0])
    need = 0
    for j in xrange(1, int(maxi) + 1):
        if people < j:
            need += (j - people)
            people = j
        people += int(aud[j])
        #print people
    outf.write('Case #%d: %d\n' % (i + 1, need))
    #print 'Case #%d: %d' % (i + 1, need)
inf.close()
outf.close()
