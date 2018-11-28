import time


def tidiness(a):
    flg = True
    tmp = 0
    cnt = 0
    for _ in a:
        c = int(_)
        if c >= tmp:
            tmp = c
            cnt += 1
    if cnt == len(a):
        flg = False
    return flg

tc = int(input())

for _ in range(tc):
    a = int(input())
    while tidiness(str(a)):
        a -= 1
    print("Case #" + str(_ + 1) + ": " + str(a))
