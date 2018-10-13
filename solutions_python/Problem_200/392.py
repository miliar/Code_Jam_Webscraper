import sys


def main():
    infile = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
    T = int(next(infile))
    for case_no in xrange(1, T+1):
        S = next(infile).strip()
        print 'Case #%d: %s' % (case_no, solve(S))
   
def solve (s):
    for i in xrange(1, len(s)):
        if s[-i] < s[-i-1]:
            head_str = s[:-i]
            head_int = int(head_str)-1 if head_str else 0
            s = (str(head_int) if head_int else '') + '9'*i
    return s 


if __name__ == '__main__':
    main()
