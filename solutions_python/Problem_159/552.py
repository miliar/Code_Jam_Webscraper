#! /usr/local/python

def method_one(l):
    result = 0
    i = 0
    while(i < len(l) - 1):
        if (l[i] - l[i+1]) >= 0:
            result += (l[i] - l[i+1])
        i+=1
    return result

assert(method_one([10, 5, 15, 5]) == 15)
assert(method_one([100, 100]) == 0)
assert(method_one([81, 81, 81, 81, 81, 81, 81, 0]) == 81)
assert(method_one([23, 90, 40, 0, 100, 9]) == 181)


def method_two(l):
    result = 0
    i = 0
    rate = 0
    while(i < len(l) - 1):
        if (l[i] - l[i+1]) > rate:
            rate = (l[i] - l[i+1])
        i+=1
    i = 0
    while(i < len(l) - 1):
        if l[i] <= rate:
            result += l[i]
        else:
            result += rate
        i+=1
    return result

assert(method_two([10, 5, 15, 5]) == 25)
assert(method_two([100, 100]) == 0)
assert(method_two([81, 81, 81, 81, 81, 81, 81, 0]) == 567)
assert(method_two([23, 90, 40, 0, 100, 9]) == 244)

T = int(raw_input())
for test in range(T):
    N = int(raw_input())
    l = [int(x) for x in raw_input().split()]
    print 'Case #%d:' % (test+1),
    print method_one(l), method_two(l)
