#!/usr/bin/env python

def read():
    r1 = int(raw_input()) - 1
    b1 = []
    for i in range(4):
        b1.append(map(int, raw_input().split()))
    
    r2 = int(raw_input()) - 1
    b2 = []
    for i in range(4):
        b2.append(map(int, raw_input().split()))

    return r1, b1, r2, b2


def work(cases, (r1, b1, r2, b2)):
    cnt = 0
    ans = -1
    
    for c1 in range(4):
        for c2 in range(4):
            if b1[r1][c1] == b2[r2][c2]:
                cnt += 1
                ans = b1[r1][c1]
    
    print "Case #%d:" % cases,
    
    if cnt == 0:
        print "Volunteer cheated!"
    elif cnt == 1:
        print ans
    else:
        print "Bad magician!"


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
