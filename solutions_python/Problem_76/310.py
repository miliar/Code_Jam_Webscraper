#!/usr/bin/python
import sys

def process(seq):
    ret = reduce(lambda x,y:x^y, seq) 
    if ret != 0:
        return "NO"
    else:
        return sum(seq)-min(seq)

def main():
    if len(sys.argv) < 2:
        print "Usages: %s IN" % sys.argv[1]
        sys.exit(1)

    fin = open(sys.argv[1])
    icases = int(fin.readline().strip())
    for c in xrange(icases):
        fin.readline()
        seq = [int(x) for x in fin.readline().strip().split()]
        print "Case #%d: %s" % (c+1, process(seq))
    

if __name__ == "__main__":
    main()
