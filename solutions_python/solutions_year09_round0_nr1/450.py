import re
L, D, N = map(int, raw_input().split())
words = []
for i in range(D):
    words.append(raw_input())
words = '\n'.join(words)
for i in range(1, N+1):
    print "Case #"+str(i)+":", len(re.findall(raw_input().replace('(', '[').replace(')', ']'), words))