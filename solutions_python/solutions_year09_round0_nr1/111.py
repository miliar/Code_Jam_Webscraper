import re

l, d, n = map(int, raw_input().split(' '))

dictionary = []

for i in range(d):
    dictionary.append(raw_input())

for i in range(n):
    pattern = raw_input()
    pattern = pattern.replace('(', '[')
    pattern = pattern.replace(')', ']')
    nummatch = 0
    for j in range(d):
        if re.match('^' + pattern + '$', dictionary[j]):
            nummatch = nummatch + 1
    print "Case #%d: %d"%(i + 1, nummatch)
