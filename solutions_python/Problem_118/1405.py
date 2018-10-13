import sys
import math


INFILE =  sys.argv[1] if len(sys.argv) >= 2 else 'teste.in'
OUTFILE = INFILE.replace('in', 'out')

in_f = open(INFILE, 'r')
out_f = open(OUTFILE, 'w')
    

def read_vec(sep=' '):
    return tuple(int(i) for i in in_f.readline().split(sep))
    

def print_line(*args):
   out_f.write("Case #%s: %s" % args + '\n')


def ispalindrome(i):
    i = str(i)
    return i == i[::-1]


def main():
    ncases = int(in_f.readline())
    for case in xrange(1, ncases+1):
        a, b = map(lambda i: math.sqrt(i), read_vec())
        a = math.ceil(a)
        b = math.floor(b)
        
        count = 0
        for i in xrange(a, b + 1):
            if ispalindrome(i) and ispalindrome(i*i):
                count += 1

        print_line(case, count)
        

if __name__ == '__main__':
    main()

in_f.close()
out_f.close()
