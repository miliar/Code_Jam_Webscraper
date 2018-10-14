import re
l, d, n = map(int, raw_input().split())
words = []
for x in xrange(d):
    words.append(raw_input())
tests = []
for x in xrange(n):
    test = re.compile(raw_input().replace('(', '[').replace(')', ']') + '$')
    count = 0
    for word in words:
        if test.match(word):
            count += 1
    print 'Case #%d: %d' % (x + 1, count)
