import sys

def main():
    inFile = open(sys.argv[1], 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N,K = map(int, inFile.readline().strip().split(' '))
        r = (K % (2**N))==(2**N-1)
        outFile.write('Case #%d: %s\n' % (t, (r and "ON" or "OFF")))
    outFile.close()
        

if __name__ == '__main__':
    main()
