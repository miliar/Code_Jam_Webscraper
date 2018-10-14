import sys, os
f = open('A-large.in', 'r')
out = open('a.out', 'w')
sys.stdout = out
sys.stdin = f
input = sys.stdin.readline
t = int(input())

for i in xrange(t):
    s = input().split()
    n, m = map(int, s)
    tree = {}
    count = 0
    print "Case #%d:" % (i+1),
    for j in xrange(n):
        exist = input().strip()[1:].split('/')
        itree = tree
        for dir in exist:
            if not itree.has_key(dir):
                itree[dir] = {}
            itree = itree[dir]
    for k in xrange(m):
        mkdir = input().strip()[1:].split('/')
        itree = tree
        for dir in mkdir:
            if itree.has_key(dir):
                itree = itree[dir]
            else:
                itree[dir] = {}
                itree = itree[dir]
                count = count + 1
            
    print count

f.close()
out.close()