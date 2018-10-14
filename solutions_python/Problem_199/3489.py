#oversized pancake flipper

n = input()

for i in xrange(n):
    panstr, k = raw_input().split()
    k = int(k)
    panstr = [p for p in panstr]
    pl = len(panstr)
    count = 0
    for j in xrange(pl - k + 1):
        #print j
        if panstr[j] == '-':
            for l in xrange(k):
                if panstr[j + l] == '-':
                    panstr[j + l] = '+'
                else:
                    panstr[j + l] = '-'
            count += 1
    #print panstr
    if '-' in panstr:
        print 'Case #' + str(i + 1) + ': IMPOSSIBLE'
    else:
        print 'Case #' + str(i + 1) + ': ' + str(count)
