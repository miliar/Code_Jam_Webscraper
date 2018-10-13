#!/usr/bin/python
import io

def is_tidy(N):
    prev = None
    for ch in str(N):
        if prev == None:
            prev = ch
            continue

        if int(prev) > int(ch):
            return False

        prev = ch

    return True

T = int(raw_input())

for current_T in range(1, T + 1):
    N = int(raw_input())

    if N < 10:
        print 'Case #%d: %d' % (current_T, N)
        continue

    number_of_9 = 0

    while is_tidy(N) == False:
        number_of_9 += 1
        R = N % 10
        N = N / 10

        if R != 9:
            N -= 1

    N = str(N)
    if N == '0': N = ''
    print 'Case #%d:' % current_T, N + ('9' * number_of_9)

    # 111111111111111110
    # 111111111111111109
    # 99999999999999999
    # 203
    # 20 9
    # 1 9
    # 528
    # 51 9
    # 4 9

