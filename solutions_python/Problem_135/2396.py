#!/usr/bin/python3

t = int(input())

for i in range(0, t):
    ans0 = int(input())
    a = [[int(_) for _ in input().split(' ')] for _ in range(0, 4)]
    ans1 = int(input())
    b = [[int(_) for _ in input().split(' ')] for _ in range(0, 4)]
    res = set(a[ans0-1]).intersection(b[ans1-1])
    if not res:
        print ("Case #%s: Volunteer cheated!" % (i + 1))
    elif len(res) > 1:
        print ("Case #%s: Bad magician!" % (i + 1))
    else:
        print ("Case #%s: %s" % ((i + 1), res.pop()))
