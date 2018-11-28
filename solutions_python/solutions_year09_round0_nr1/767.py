# Alien Language

import re

f = open ('A-large.in', 'r')
num = f.readline ()
part = num.partition (' ')
L = int (part[0])
part = part[2]
part = part.partition (' ')
D = int (part[0])
part = part[2]
part = part.partition ('\n')
N = int (part[0])

cnt = 0
words = list ()
for line in f:
    words.append (line[0:L])
    cnt +=1
    if cnt == D:
        break

cnt = 1
for line in f:
    reg_expr = line[0:len(line)-1]
    reg_expr = reg_expr.replace ('(', '[') 
    reg_expr = reg_expr.replace (')', ']') 
    pattern = re.compile (reg_expr)

    num = 0
    found = 0
    while num < D:
        match = pattern.match (words[num])
        if match:
            found = found + 1
        num += 1

    print "Case #%d: %d" % (cnt, found)
    cnt += 1

f.close()
