import sys

input_ = sys.stdin
#input_ = open('test.txt')
#input_ = open('A-small-practice.in.txt')
#input_ = open('A-large-practice.in.txt')

def input():
    return input_.readline()

def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_line():
    return input().rstrip('\n')

def read_words(sep=' '):
    return read_line().split(sep)

# solution-specific functions

T = read_int()
for t in xrange(1, T + 1):
    # solution-specific code
    smax, s = read_words()
    smax = int(smax)
    s = map(int, s)
    standing = 0
    added = 0
    for i in xrange(0, smax + 1):
        if standing < i and s[i] > 0:
            added += i - standing
            standing += added
        standing += s[i]
            
#    print smax, s
    print "Case #%d: %d" % (t,added)
