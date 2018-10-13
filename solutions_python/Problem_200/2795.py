#!/usr/bin/env python3
def check(n):
    temp = str(n)[::-1]
    last = temp[0]
    for i in temp[1:]:
        if i > last:
            return False
        else:
            last = i
    return True

def pss(n):
    temp = list(str(n))
    while check(int(''.join(temp))) == False:
        for i in range(len(temp)-1):
            if temp[i] > temp[i+1]:
                temp[i] = str(int(temp[i]) - 1)
                for j in range(i+1, len(temp)):
                    temp[j] = '9'
                break
    return int(''.join(temp))


for T in range(1, int(input())+1):
    num = int(input())
    res = pss(num)
    print('Case #{}: {}'.format(T, res))