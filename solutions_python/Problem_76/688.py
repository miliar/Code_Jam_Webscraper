#!/usr/bin/python -tt

import sys

def main():
    if len(sys.argv) != 2:
        print 'Requires input file'
        sys.exit()
    fname = sys.argv[1]
    fptr = open(fname, 'r')
    numtest = int(fptr.readline().split(' ')[0])
    outptr = open('output', 'w')
    for i in xrange(numtest):
        N = int(fptr.readline().split(' ')[0])
        candies = map(int, fptr.readline().split(' '))
        #print candies
        ans = reduce(lambda x,y: x^y, candies)
        if ans == 0:
            candies.remove(min(candies))
            outptr.write('Case #%d: %d\n' %(i+1, sum(candies)))
        else:
            outptr.write('Case #%d: NO\n' % (i+1))
    
    outptr.close()
    fptr.close()
        

if __name__ == '__main__':
    main()