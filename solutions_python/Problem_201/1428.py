# -*- coding: utf-8 -*-

def get_result(n):
    if n % 2:
        return n // 2, n // 2
    else:
        return n // 2, n // 2 - 1

def solution(n, k):
    k -= 1
    if not k:
        return get_result(n)
    if n % 2:
        big = n // 2
        big_n = 2
        small = None
        small_n = 0
    else:
        big = n // 2
        big_n = 1
        small = n // 2 - 1
        small_n = 1

    while True:
        if k <= big_n:
            return get_result(big)
        else:
            k -= big_n
            if k <= small_n:
                return get_result(small)
            else:
                k -= small_n

        if big % 2:
            big //= 2
            big_n = big_n * 2 + small_n
            small = big - 1
            #small_n = small_n
        else:
            big //= 2
            #big_n = big_n
            small = big - 1
            small_n = small_n * 2 + big_n

import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit()

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file, 'r') as f:
        length = int(f.readline().strip())
        l = []
        for _ in range(length):
            line = f.readline().strip()
            n, k = line.split(' ')
            l.append([int(n), int(k)])

    print('l = ', l)
    result = []
    for n, k in l:
        result.append(solution(n ,k))
    print('result = ', result)

    with open(out_file, 'w') as of:
        length = len(result)
        for i in range(length):
            s = 'Case #' + str(i + 1) + ': ' + str(result[i][0]) + ' ' + str(result[i][1]) + '\n'
            of.write(s)
