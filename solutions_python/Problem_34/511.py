import re
import sys

def makeor(m):
    return '(' + '|'.join(list(m.groups()[0])) + ')'

findor = re.compile("\((.*?)\)")
l, d, n = [int(x) for x in raw_input().split()]

words = ""

for x in xrange(d):
    words+=(sys.stdin.readline())

for x in xrange(n):
    case = sys.stdin.readline().strip()
    regex = findor.sub(makeor, case)
    print "Case #%d: %d" % (x+1, len(re.findall(regex, words)))   

