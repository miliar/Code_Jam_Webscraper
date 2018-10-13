import sys



inputfile = open(sys.argv[1], 'r')
cases = int(inputfile.readline())

def rn(n):
    return (n)[1:]+str(n)[0]


for i in range(cases):
    [a,b] = [int(n) for n in inputfile.readline()[:-1].split()]
    n = a
    pairs = []
    while n < b:
        strn = str(n)
        for j in range(len(str(n))):
            strn = rn(strn)
            strnn = int(strn)
            #print 'trying: %s and %s is between %s and %s'%(n, strnn, a, b)
            if strnn > n and strnn <= b and strnn >= a:
                if (n,strnn) not in pairs:
                    pairs.append((n,strnn))
                    #print 'added!'

        n += 1
    print "Case #%s: %s"%(i+1, len(pairs))        
    #print pairs




