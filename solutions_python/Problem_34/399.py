# Alien language with exactly D words with all exactly L lowercase letters.
# N test cases.

import sys
import re

def read_metadata():
    line = sys.stdin.readline()
    parts = line.split(' ')
    return int(parts[0]), int(parts[1]), int(parts[2])

def read_words(D, L):
    return [sys.stdin.readline().strip() for x in xrange(D)]

def read_tests(N, L):
    def sanitize(val):
        regex = val.strip().replace('(', '[').replace(')', ']')
        return re.compile(regex)
    return [(x+1, sanitize(sys.stdin.readline())) for x in xrange(N)]

if __name__=='__main__':
    L, D, N = read_metadata()
    words = read_words(D, L)
    tests = read_tests(N, L)
    for num, prog in tests:
        count = 0;
        for word in words:
            if prog.match(word):
                count += 1
        print "Case #%d: %d" % (num, count)
