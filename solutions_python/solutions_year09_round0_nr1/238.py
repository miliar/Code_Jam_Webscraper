#-*-coding:utf-8-*-
import sys, re
fh = open(sys.argv[1])
L, D, N = map(int,fh.readline().split(' '))
words = []
for i in range(D): words.append(fh.readline().strip())
for i in range(N):
    pattern=fh.readline().strip()
    reg = re.compile(re.sub('\\)', ']', re.sub('\\(', '[',pattern)))
    n = 0
    for w in words:
        if reg.match(w): n += 1
        pass
    print("Case #%d: %d" % (i + 1, n))
