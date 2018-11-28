from sys import stdin
from pprint import pprint

def insert(root, name):
    path = name.split('/')[1:]
    cur = root
    counter = 0
    for d in path:
        if d not in cur:
            cur[d] = {}
            counter += 1
        cur = cur[d]
    return counter

tests = int(stdin.readline())
for test in xrange(1, tests + 1):
    N, M = map(int, stdin.readline().split())
    root = {}
    for _ in xrange(N):
        insert(root, stdin.readline().strip())
    total = 0
    for _ in xrange(M):
        total += insert(root, stdin.readline().strip())
    root = {}
    print "Case #%d: %d" % (test, total)
