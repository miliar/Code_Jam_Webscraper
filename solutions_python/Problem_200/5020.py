#!/usr/bin/python
import sys

# Part of 2016 Google code jam
# Find last "tidy" number (digits increment) in a range


def find_tidy(n):
    while n != 0:
        dec = is_tidy(n)

        if dec == -1:
            return n
        else:
            n = n - dec
    return n

def is_tidy(i):
    a = list(str(i))

    prev = list(a)
    a.sort()

    if prev == a:
        return -1
    else:
        l = len(a)

        for j in range(1,l-1):
            if int(prev[j]) > int(prev[j+1]):
                end = int(''.join(prev[l-j:])) + 1
                return end
   
        return 1 

T = int(raw_input().strip())

for i in range(1, T+1):
    n = int(raw_input().strip())
    result = find_tidy(n)
    print 'Case #' + str(i) + ': ' + str(result)
