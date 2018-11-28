#!/usr/bin/python


def divide(n):
    mod = n & 1
    div = n >> 1
    return (div + mod, div)

def pop_max(_list):
    _list.sort(reverse=True)
    return _list.pop(0)

def calc(list_N, K):
    while K > 0:
        _max, _min = divide(pop_max(list_N) - 1)
        list_N.append(_max)
        list_N.append(_min)
        K = K - 1
    return _max, _min

def main():
    line = raw_input()
    T = int(line)
    for t in range(1, T + 1):
        line = raw_input()
        arr = line.split()
        N = int(arr[0])
        K = int(arr[1])
        _max, _min = calc([N], K)
        print('Case #%d: %d %d' % (t, _max, _min))

if __name__ == '__main__':
    main()
