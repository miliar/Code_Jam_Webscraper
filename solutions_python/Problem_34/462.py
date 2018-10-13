import re
L, D, N = [int(i) for i in raw_input().split(' ')]
lexis = []
for i in range(D):
    lexis.append(raw_input())
for i in range(N):
    count = 0
    item = raw_input()
    reg = re.compile(r"^%s$" % item.replace('(', '[').replace(')', ']'))
    for j in lexis:
        if reg.match(j) !=  None:
            count = count + 1
    print 'Case #%s: %s\n' % (i+1, count)
