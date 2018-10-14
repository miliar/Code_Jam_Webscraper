
import os, sys, re, string

def pattern_convert(s):
    return re.compile(s.replace('(', '[').replace(')', ']'))

def main():
    L,D,N = map(lambda x: int(x), sys.stdin.readline().split(" "))
    texts = map(lambda x: sys.stdin.readline().strip(), range(D))
    raw_patterns = map(lambda x: pattern_convert(sys.stdin.readline().strip()), range(N))
    for i in range(N):
        pattern = raw_patterns[i]
        count = len(filter(lambda x: pattern.match(x), texts))
        print "Case #%d: %d" % (i + 1, count)
     
if __name__ == '__main__':
    main()
