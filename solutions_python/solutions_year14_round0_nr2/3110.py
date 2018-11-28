'''
Created on Apr 13, 2012

@author: yonch
'''


def eat(lines):
    return lines[0], lines[1:]
 
def do(l):
    l = map(float,l.split(' '))
    C, F, X = l[:3]
    l = l[3:]
    
    base = 0
    A = []
    for n in xrange(150000):
        A.append(base + (X / (2.0 + n*F)))
        base += (C / (2.0 + n*F))
    
    n = 0
    base = 0
    while True:
        no_buy = base + (X / (2.0 + n*F))
        buy = base + (C / (2.0 + n*F)) + (X / (2.0 + (n + 1) * F))
        if buy >= no_buy:
            if abs(no_buy - min(A)) > 1e-6:
                print "%.9f %.9f" % (no_buy, min(A))#, A
                exit
            return "%.9f" % no_buy
        
        base += (C / (2.0 + n*F))
        n = n + 1
        #print "n =",n, "base =", base, "buy =", buy, "no_buy =",no_buy
        
    
def read():
    return """4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0""".splitlines()

def readf():
    INPUT_FILENAME = '/home/yonch/Downloads/B-large (1).in'
    return file(INPUT_FILENAME).read().splitlines()

if __name__ == '__main__':
    lines = readf()
    line, lines = eat(lines)
    N = int(line)
    outfile = ""
    for i in xrange(N):
        line, lines = eat(lines)
        outline = "Case #%d: %s" % (i+1, do(line))
        print outline
        outfile += outline + "\n"
    
    file('/home/yonch/workspace/codejam/Solution.out','w').write(outfile)