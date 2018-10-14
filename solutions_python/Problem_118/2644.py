import math
import sys

if len(sys.argv) < 2:
    print 'Missing filename argument.'
    sys.exit(1)

def is_palindrome(seq):
    fp = 0
    bp = len(seq) - 1
    while fp < bp:
        if seq[fp] != seq[bp]:
            return False
        fp += 1
        bp -= 1
    return True

with open(sys.argv[1]) as fh:
    lines = fh.readlines()[1:]
    
    idx = 1
    for line in lines:
        print 'Case #%d: ' % (idx,),
        count = 0
        rs, re = map(int, line.split())
        for num in xrange(rs, re+1):
            if is_palindrome(str(num)):
                sqrt = math.sqrt(num)
                if sqrt.is_integer():
                    if is_palindrome(str(int(sqrt))):
                        count += 1
        print count
        idx += 1
                
