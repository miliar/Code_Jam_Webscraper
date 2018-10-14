from sys import *

def xor_list(x):
    """
    XORs a list, returns the final value
    """
    state = 0
    for i in x:
        state = state ^ i

    return state

def find_max_bag(x):
    """
    Find the minimum matching XOR value in a list, summing the rest
    """
    mylist = x
    mylist.sort()
    first = mylist.pop(0) # pop off the first element

    state = 0
    for i in mylist:
        state = state ^ i

    if state == first:
        return sum(mylist)
    else:
        return "NO"

cases = int(raw_input())

for _ in xrange(cases):
    total_candy = int(stdin.readline())
    candies = map(int, stdin.readline().split())

    xor = xor_list(candies)
    
    if xor == 1:
        result = "NO"
    else:
        result = find_max_bag(candies)

    print "Case #%d: %s" % (_+1, result)
