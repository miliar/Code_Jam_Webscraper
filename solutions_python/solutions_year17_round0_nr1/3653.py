inpFile = open('A-small-attempt1.in', 'r')
try:
    t = int(inpFile.readline())
    for case in xrange(t):
        flips = 0
        pancakes, k = inpFile.readline().split(' ')
        k = int(k)
        pancakes = list(pancakes)
        for i in xrange(len(pancakes) - k + 1):
            if pancakes[i] == '-':
                flips += 1
                for j in xrange(i, i+k):
                    if pancakes[j] == '-':
                        pancakes[j] = '+'
                    else:
                        pancakes[j] = '-'
        if '-' not in pancakes:
            print 'Case #%d: %d'%(case+1, flips) 
        else:
            print 'Case #%d: %s'%(case+1, 'IMPOSSIBLE')
except EOFError:
    print 'done'
