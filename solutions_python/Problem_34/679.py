import re

fin = open('A-large.in')

l, d, n = map(int, fin.readline().strip().split())

words = []
for i in range(d):
    words.append(fin.readline().strip())
    
case = 0

for i in range(n):
    ans = 0
    s = '^' + fin.readline().strip().replace('(','[').replace(')',']') + '$'
    for word in words:
        if (re.match(s, word)):
            ans+=1
    case += 1
    print 'Case #%d: %d' % (case, ans)
