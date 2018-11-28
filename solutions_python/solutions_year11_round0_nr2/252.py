#Google Codejam Problem B. Magicka

from cStringIO import StringIO
from sys import stdin
from collections import defaultdict

def combinable(item):
    return len(out) >= 1 and combi.has_key(item + out[-1])

def conflict(item):
    return any(item in enemy[x] for x in out)

cases = int(stdin.readline())

for caseNo in xrange(1, cases+1):
    #reading/parsing IO
    input = iter(stdin.readline().split()).next
    combines = int(input())
    combi = dict()
    for _ in xrange(combines):
        st = input()
        ab = st[:2]
        combi[ab] = combi[ab[::-1]] = st[-1]
    conflicts = int(input())
    enemy = defaultdict(set)
    for _ in xrange(conflicts):
        st = input()
        enemy[st[0]].add(st[1])
        enemy[st[1]].add(st[0])
    sequenceLenght = int(input())
    sequence = input()
    #computing the answer
    out = []
    for item in sequence:
        
        while combinable(item):
            item = combi[item + out[-1]]
            out.pop()
        if conflict(item):
            out = []
        else:
            out.append(item)
        #print item, out
    print "Case #%d: [%s]" % (caseNo, ', '.join(out))
