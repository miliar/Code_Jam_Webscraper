import sys
import bisect

palindrome = []
valid = []
for i in xrange(1, 10**7 + 1):
    s = str(i)
    r = s[::-1]
    if s == r:
        palindrome.append(i)

for i in palindrome:
    square = i * i
    if square > 10 ** 14:
        break
    s = str(square)
    r = s[::-1]
    if s == r:
        valid.append(square)

T = int(raw_input())
for i in xrange(1, T + 1):
    A, B = map(int, raw_input().split())
    start = bisect.bisect_left(valid, A)
    end = bisect.bisect_right(valid, B)
    print "Case #{0}: {1}".format(i, end - start)
