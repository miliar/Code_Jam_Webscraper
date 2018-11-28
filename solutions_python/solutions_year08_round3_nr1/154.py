#!/usr/bin/env python

def calc_keys(arr, num, key):
    arr.sort()
    arr = arr[::-1]
    length = len(arr)
    barr = []
    def gen_barr():
        for i in range(num):
            for j in range(key):
                barr.append(i + 1)
                if len(barr) == length:
                    return
    gen_barr()
    s = 0
    for i in range(length):
        s += arr[i] * barr[i]
    return s

if __name__ == '__main__':
    caseno = int(raw_input())
    for i in range(caseno):
        l = raw_input().split(' ')
        num = int(l[0])
        key = int(l[1])
        arr = [int(x) for x in raw_input().split(' ')]
        print 'Case #%d: %d' % (i + 1, calc_keys(arr, num, key))
