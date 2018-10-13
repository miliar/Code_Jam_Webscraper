import math

def first(inter, left):
    eaten = 0
    for i in xrange(1, inter):
        if left[i] < left[i-1]:
            eaten += left[i-1] - left[i]
    return eaten

def second(inter, left):
    maxdiff = 0
    eaten = 0
    for i in xrange(1, inter):
        if left[i] < left[i-1]:
            if left[i-1] - left[i] > maxdiff:
                maxdiff = left[i-1] - left[i]
    rate = maxdiff/10.
    for j in xrange(1, inter):
        diff = left[j-1] - left[j]
        eaten += min(left[j-1], rate * 10)
    return eaten

def analysis():
    intervals = int(raw_input())
    left = map(int, raw_input().split())
    return (first(intervals, left), second(intervals, left))

cases = int(raw_input())

for i in xrange(cases):
    x, y = analysis()
    output = "Case #%i: %i %i" % (i+1, x, y)
    print output
