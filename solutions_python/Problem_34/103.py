import sys
import re

L,D,N = map(int, re.findall(r'\d+', raw_input()))

dic = []
for x in range(D):
   dic.append(raw_input())

for i in range(1,N+1):
    rex = raw_input()
    rex = rex.replace("(","[",5000).replace(")","]",5000)

    cnt = 0
    for j in range(D):
        if re.match(rex, dic[j]) is not None:
            cnt += 1

    print "Case #%d: %d" % (i,cnt)
