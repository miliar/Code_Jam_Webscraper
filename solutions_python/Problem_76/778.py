import sys
def main():
    file = sys.argv[1]
    f = open(file, 'r')
    cases = int(f.readline())
    
    for case in xrange(cases):
        candies = int(f.readline())
        values = [int(x) for x in f.readline().split()]
        xor = 0
        sum = 0
        min = None
        for v in values:
            xor = xor ^ v
            sum += v
            if not(min) or v < min: min = v
        
        if xor == 0: 
            s = sum - min
        else:
            s = "NO"
        
        print "Case #%d: %s" % (case + 1, s)

if __name__ == "__main__":
    sys.exit(main())
