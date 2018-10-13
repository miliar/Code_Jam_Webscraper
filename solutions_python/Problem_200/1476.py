# -*- coding: utf-8 -*-

import sys

#def solution(s):
#    length = len(s)
#    t = length - 1
#    for i in range(length - 2, -1, -1):
#        j = i - 1
#        if int(s[i]) <= int(s[j]):
#            continue
#        else:
#            t = i

def solution(i):
    l = []
    while i:
        l.append(i % 10)
        i //= 10

    length = len(l)
    t = 0
    for j in range(1, length):
        k = j - 1
        if l[j] <= l[k]:
            continue
        else:
            t = j
            l[j] -= 1
    for j in range(t):
        l[j] = 9

    s = 0
    for j in range(length - 1, -1, -1):
        s *= 10
        s += l[j]

    return s

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit()
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    l = []
    with open(in_file, 'r') as f:
        length = int(f.readline().strip())
        for _ in range(length):
            l.append(int(f.readline().strip()))

    print('l = ', l)
    r = []
    for i in l:
        j = solution(i)
        print('j = ', j)
        r.append(j)

    with open(out_file, 'w') as of:
        length = len(r)
        for i in range(length):
            s = 'Case #' + str(i + 1) + ': ' + str(r[i]) + '\n'
            of.write(s)
