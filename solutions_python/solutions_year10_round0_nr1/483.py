def SNAPPER(filename):
    f = open(filename, 'r')
    g = open('A-large.out','w')
    numbers = f.readline()
    t = int(numbers)
    for i in range(0,t):
        line = f.readline()
        nk = line.split(' ')
        n = int(nk[0])
        k = int(nk[1])
        ideal = 2**n
        if k % ideal == ideal - 1:
            g.write('Case #%s: ON\n' % (i+1))
        else:
            g.write('Case #%s: OFF\n' % (i+1))
        
SNAPPER('A-large.in')
