#!/usr/bin/python3

cases = int(input())

for case in range (1, cases + 1):

    row = int(input()) - 1
    for x in range(4):
        line = input()
        if x == row:
            candidates = set(line.split())

    #print(candidates)
    row2 = int(input()) - 1
    for x in range(4):
        line = input()
        if x == row2:
            candidates2 = set(line.split())
    #print(candidates2)

    results = candidates & candidates2
    #print(results)
    if len(results) == 1:
        answer = results.pop()
    elif len(results) == 0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"

    print("Case #%s: %s" % (case, answer))
