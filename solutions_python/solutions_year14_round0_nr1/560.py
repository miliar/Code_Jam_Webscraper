#!/usr/bin/env python3

T = int(input())
for t in range(1, T+1):
    answer = "x"
    r1 = int(input())
    for i in range(1,5):
        line = input()
        if r1 == i:
            s1 = set(list(map(lambda x:int(x), line.strip().split())))
    r2 = int(input())
    for i in range(1, 5):
        line = input()
        if r2 == i:
            s2 = set(list(map(lambda x:int(x), line.strip().split())))
    answer = s1 & s2
    if len (answer) == 0:
        answer = "Volunteer cheated!"
    elif len(answer) == 1:
        answer = answer.pop()
    else:
        answer = "Bad magician!"
    print("Case #%d: %s" % (t, answer))

