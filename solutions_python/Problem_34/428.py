import re

line = raw_input()
ldn = line.split(' ')
# print ldn
l = int(ldn[0])
d = int(ldn[1])
n = int(ldn[2])
# print l + d
dictionary = []
while d > 0:
    dictionary.append(raw_input())
    d -= 1
# print dictionary
testcases = []
while n > 0:
    testcases.append('^' + raw_input().replace('(','[').replace(')',']') + '$')
    n -= 1
# print testcases
i = 0
for t in testcases:
    cnt = 0
    regex = re.compile(t)
    for word in dictionary:
        if regex.match(word) is not None:
            cnt += 1
    i += 1
    print 'Case #%d: %d' % (i, cnt)
