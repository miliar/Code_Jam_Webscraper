#!/usr/bin/python
for i in range(int(input())):
    first = int(input())
    cards1 = [ map(int, input().split()) for _ in range(4) ]
    second = int(input())
    cards2 = [ map(int, input().split()) for _ in range(4) ]
    candidate = set(cards1[first-1]) & set(cards2[second-1])
    if len(candidate) == 1:
        res = list(candidate)[0]
    elif len(candidate) > 1:
        res = 'Bad magician!'
    else:
        res = 'Volunteer cheated!'
    print('Case #{0}: {1}'.format(i+1, res))
