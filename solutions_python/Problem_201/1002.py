
def flip(x):
    c = ''
    for e in x:
        if e == '+':
            c+= '-'
        else:
            c+='+'
    return c

def pancake(s, k):
    if set(s) == {'+'}:
        return 0
    c = 0
    i = s.index('-')
    while i <= len(s) - k:
        temp = s[i:i+k]
        prev = s[:i]
        next = s[i+k:]
        s = prev + flip(temp) + next
        c += 1
        if set(s) == {'+'}:break
        i = s.index('-')
    if set(s) == {'+'}: return c
    return 'IMPOSSIBLE'


def tidy(n):
    if n < 10: return n
    n = list(str(n))
    l = n[-1]
    index = len(n) - 2
    for e in n[::-1][1:]:
        if e > l:
            n[index] = str(int(e) - 1)
            for i in range(index+1, len(n)):
                n[i] = '9'
        l = n[index]
        index -= 1
    return int(''.join(n))

from heapq import heappush as push
from heapq import heappop as pop

def bathroom(n, k):
    heap = []
    push(heap, -n)
    for i in range(k-1):
        num = -pop(heap)
        h = num/2
        if num % 2 == 0:
            push(heap, -h)
            push(heap, -h + 1)
        else:
            push(heap, -h)
            push(heap, -h)
    num = -pop(heap)
    if num % 2 == 0:
        return num/2, num/2 - 1
    return num/2, num/2

from math import log
def bathroom2(n, k):
    m = 2**int(log(k, 2) + 1)
    x = n*2/m - 1
    b = n+1 - m/2 - (m/2)*x
    a = m/2 - b
    r = m/2
    if b > k - r:
        x += 1
    if x % 2 == 0:
        return x/2, x/2 - 1
    return x/2, x/2


n = int(raw_input().strip())
for i in range(n):
    num, k = map(int, raw_input().strip().split())
    l, r = bathroom2(num, k)
    print 'Case #%d: %d %d' % (i+1, l, r)
