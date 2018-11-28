#!/usr/bin/env python3
import bisect
import math


def isPalindrome(i):
    i = str(i)
    return i == i[::-1] # first half is last half reversed

limit = 10**14
limit = math.ceil(math.sqrt(limit))
# palindromicSquares = [1, 4, 9, 121, 484, 676, 10201, 12321, 14641, 40804, 44944, 69696, 94249, 1002001, 1234321, 4008004, 5221225, 6948496, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 522808225, 617323716, 942060249, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1086078706801, 1210024200121, 1212225222121, 1214428244121, 1230127210321, 1232346432321, 1234567654321, 1615108015161, 4000008000004, 4004009004004, 4051154511504, 5265533355625, 9420645460249]
# fairSquares = [ x for x in palindromicSquares if isPalindrome(int(math.sqrt(x)))]

#fairSquares = [ i**2 for i in range(1, limit+1) if isPalindrome(i) and isPalindrome(i**2)]
fairSquares = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]


# print(fairSquares)
# print([(math.sqrt(fs)) for fs in fairSquares])

def rangeCount(lower, upper):
    count = 0
    i=0
    while fairSquares[i] <  lower:  i+=1
    while i<len(fairSquares) and fairSquares[i] <= upper:  i+=1; count += 1
    return count


numCases = int(input())
for caseNum in range(numCases):
    # print(lower, upper)
    # index_lower = bisect.bisect_left (fairSquares, lower)
    # index_upper = bisect.bisect_right(fairSquares, upper) -1
    # print( index_lower, index_upper )
    print('Case #{0}: {1}'.format(caseNum+1, rangeCount(*map(int, input().split()))))