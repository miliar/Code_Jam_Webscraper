import re

L, D, N = map(int, raw_input().split(' '))
words = ''
for i in range(D):
    words += raw_input() + '\n'
for case in range(N):
    pattern = raw_input().replace('(', '[').replace(')', ']')
    t = re.compile('^' + pattern + '$', re.MULTILINE).findall(words)
    print 'Case #%s: %d' % (case + 1, len(t))
