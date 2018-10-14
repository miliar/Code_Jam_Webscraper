from math import *

def is_palin(n):
    forward = n
    reverse = 0
    while (n > 0):
        remainder = n % 10
        reverse = reverse*10 + remainder
        n = n / 10
    if forward == reverse:
        return True
    else:
        return False

def xlongrange(start, end):
    n = start
    while n < end:
        yield n
        n += 1

T = int(raw_input())

for i in range(T):
    A, B = map(long, raw_input().split())
    root_A = long(floor(sqrt(A)))
    root_B = long(ceil(sqrt(B)))
    #print root_B
    #print root_A, root_B

    li = []

    for n in xlongrange(root_A, root_B+1):
        if is_palin(n):
            if is_palin(n*n):
                li.append(n*n)

    print "Case #%d: %d" % (i+1, len([x for x in li if x >= A and x <= B]))

