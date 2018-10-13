import sys

def recycle(s):
    for x in xrange(1, len(s)):
        yield s[x:] + s[:x]
        
def print_case(i, a, b):
    count = 0
    for n in xrange(a, b + 1):
        s = str(n)
        for x in set(recycle(s)):
            if x[0] != '0':
                m = int(x)
                if n < m <= b:
                    count += 1
    print "Case #%d: %d" % (i, count)
    
def main():
    lines = open(sys.argv[1]).readlines()[1:]
    
    for i,line in enumerate(lines):
        print_case(i + 1, int(line.split()[0]), int(line.split()[1]))
    
if __name__ == "__main__":
    main()

