#!/usr/bin/python3
out = []

for case in range(int(input())):
    shyMax, people = input().split(' ')
    shyMax, people = int(shyMax), [int(i) for i in people]
    total = people[0]
    required = 0
    for i in range(1, shyMax+1):
        while (total < i):
            total += 1
            required += 1
        total += people[i]

    out.append("Case #{}: {}".format(case+1, required))

for case in out:
    print(case)
