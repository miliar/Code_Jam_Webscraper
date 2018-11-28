
import numpy as np


def pal_root(a):
    assert a.size % 2 == 1
    root = np.empty(a.size // 2 + 1)
    root[0] = np.sqrt(a[0])
    for i in xrange(1, root.size):
        root[i] = (a[i] - np.dot(root[1:i], root[i - 1:0:-1])) / 2 / root[0]
    for i in xrange(root.size - 1):
        frac, root[i] = np.modf(root[i])
        root[i + 1] += 10 * frac
    return root

def str_to_arr(string):
    string = string.strip()
    arr = np.empty(len(string), dtype=int)
    for i, c in enumerate(string):
        arr[i] = ord(c) - 0x30
    return arr

def cmp_arr(a1, a2):
    if a1.size < a2.size:
        return -1
    if a1.size > a2.size:
        return 1
    lower = a1 < a2
    greater = a1 > a2
    li = np.nonzero(lower)[0]
    gi = np.nonzero(greater)[0]
    if li.size <= 0 and gi.size <= 0:
        return 0
    if gi.size <= 0:
        return -1
    if li.size <= 0:
        return 1
    if li[0] < gi[0]:
        return -1
    return 1

def next_pal(a):
    while a.size % 2 == 0 or not ispal(a):
        a = inc(a)
    return a

def prev_pal(a):
    while a.size % 2 == 0 or not ispal(a):
        a = dec(a)
    return a

def rootpal_range(low, high):
    low = pal_root(next_pal(low))
    high = pal_root(prev_pal(high))
    low[-1] = np.ceil(low[-1])
    high[-1] = np.floor(high[-1])
    return low, high

def ispal(a):
    if a.size == 1:
        return True
    front_half = a.size // 2
    back_half = (a.size + 1) // 2
    front = a[:front_half]
    back = a[back_half:]
    if np.any(front != back[::-1]):
        return False
    return True

def check(a):
    if not ispal(a):
        return False
    o = np.outer(a, a[::-1])
    for i in xrange(-o.shape[0] + 1, o.shape[0]):
        if np.trace(o, i) > 9:
            return False
    return True

def incrt(a):
    for i in xrange(a.size):
        a[-i - 1] += 1
        if a[-i - 1] > 3:
            a[-i - 1] = 0
        else:
            return a
    new = np.empty(a.size + 1)
    new[0] = 1
    new[1:] = a
    return new

def inc(a):
    for i in xrange(a.size):
        a[-i - 1] += 1
        if a[-i - 1] > 9:
            a[-i - 1] = 0
        else:
            return a
    new = np.empty(a.size + 1)
    new[0] = 1
    new[1:] = a
    return new

def dec(a):
    for i in xrange(a.size):
        a[-i - 1] -= 1
        if a[-i - 1] < 0:
            a[-i - 1] = 9
        else:
            return a[np.nonzero(a)[0][0]:]
    return a[np.nonzero(a)[0][0]:]

def check_range((low, high)):
    current = low
    count = 0
    while cmp_arr(current, high) <= 0:
        if check(current):
            count += 1
        current = incrt(current)
    return count


if __name__ == '__main__':
    import sys
    T = int(sys.stdin.readline())
    for i in xrange(T):
        low, high = sys.stdin.readline().split(' ')
        print 'Case #%i: %i' % (i + 1, check_range(
            rootpal_range(str_to_arr(low), str_to_arr(high))))
