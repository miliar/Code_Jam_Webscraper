import sys


def main():
    input = sys.argv[1]
    output = sys.argv[2]
        
    ifd = open(input, 'r')
    ofd = open(output, 'w')
    
    T = int(ifd.readline())
    
    for t in range(T):
        N = int(ifd.readline())
        xstring = ifd.readline().split()
        ystring = ifd.readline().split()
        x = []
        y = []
        for n in range(N):
            x.append(int(xstring[n]))
            y.append(int(ystring[n]))
            
        x.sort()
        y.sort()
        y.reverse()
        
        p = 0
        for n in range(N):
            p += (x[n] * y[n])
        print "Case #%d: %d" % (t + 1, p)
        ofd.write("Case #%d: %d\n" % (t + 1, p))
    ifd.close()
    ofd.close()
main()

