#!/usr/bin/env python3

def correct(num):
    bad_pos = None
    num = [int(i) for i in num]
    for i in range(len(num) - 1):
        if num[i + 1] < num[i]:
            bad_pos = i
            break
    if bad_pos is None:
        return ''.join(str(i) for i in num)

    bad_pos -= 1
    while bad_pos >= 0 and num[bad_pos] == num[bad_pos + 1]:
        bad_pos -= 1
    bad_pos += 1

    if num[bad_pos] == 1:
        return '9' * (len(num) - 1)

    num[bad_pos] -= 1
    for i in range(bad_pos + 1, len(num)):
        num[i] = 9
    
    return ''.join(str(i) for i in num)

for i in range(int(input())):
    print('Case #{}: {}'.format(i + 1, correct(input())))
