import re

(L,D,N) = [int(temp) for temp in raw_input().split(' ')]
words = []

for x in xrange(0,D):
    words.append(raw_input())

for x in xrange(0,N):
    count = 0
    pattern = raw_input()
    pattern = pattern.replace('(','[')
    pattern = pattern.replace(')',']')
    for word in words:
        if re.match(pattern,word):
            count += 1

    print "Case #"+str(x+1)+": "+str(count)
