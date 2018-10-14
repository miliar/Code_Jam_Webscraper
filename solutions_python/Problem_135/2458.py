#!/usr/bin/python


def find_answer():
    a = int(raw_input())
    am = [[int(x) for x in raw_input().split()] for i in range(4)]
    b = int(raw_input())
    bm = [[int(x) for x in raw_input().split()] for i in range(4)]
    la = set(am[a-1])
    lb = set(bm[b-1])
    li = list(la & lb)
    if len(li) == 1:
        return str(li[0])
    elif len(li) == 0:
        return C3
    else:
        return C2

T = int(raw_input())
C2 = 'Bad magician!'
C3 = 'Volunteer cheated!'

for i in range(T):
    ans = find_answer()
    print('Case #' + str(i + 1) + ': ' + ans)
