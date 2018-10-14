import os, sys

lines = sys.stdin.read().split('\n')

lines.pop(0)

case = 0
for line in lines:
    if not line:
        break
    case += 1
    auds = line.split().pop()
    add = 0
    sum = 0
    for level in range(len(auds)):
        if (level > sum + add):
            add += level - (sum + add)
        sum += int(auds[level])

    print "Case #%d: %d" % (case, add)
