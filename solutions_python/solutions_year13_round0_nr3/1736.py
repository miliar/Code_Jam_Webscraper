import sys
import math
import bisect
import random

def isPalindrome(s):
    return s == s[::-1]

def doit(a, b):
    result = 0
    position = 0

    # find highest square less than "a"
    root = int(math.sqrt(a))
    square = root*root
    if square == a:
        root -= 1
        square = root*root
    increment = 2*root+1

    while square <= b:
        while position < len(sorted_a) and square >= sorted_a[position][0]:
            position +=1

        if position < len(sorted_a) and sorted_a[position][0] <= square+increment <= sorted_a[position][1] and sorted_a[position][1] <= b:
            result += intervals[(sorted_a[position][0], sorted_a[position][1])]
            root = sorted_a[position][2]
            square = root*root
            increment = 2*root+1
            position += 1
        else:
            root += 1
            square += increment
            increment += 2
            if isPalindrome(str(root)) and isPalindrome(str(square)) and square <= b:
                result += 1

    return result, root-1

intervals = {}
sorted_a = []

tests = int(sys.stdin.readline())
for i in range(1, tests+1):
    output = "Case #" + str(i) + ":"
    result = 0

    line = sys.stdin.readline().split()
    a = int(line[0])
    b = int(line[1])

    result = doit(a, b)

    intervals[(a,b)] = result[0]
    bisect.insort(sorted_a, (a, b, result[1]))
    print(output, result[0])

def tests(n):

    for i in range(n):
        a = random.randrange(1, 1000)
        b = random.randrange(a+1, 10000)
        c = random.randrange(b+1, 100000)

        result1 = doit(a,b)
        intervals[(a,b)] = result1[0]
        bisect.insort(sorted_a, (a, b, result1[1]))
        print(a, result1[0])

        result2 = doit(b+1,c)
        intervals[(b+1,c)] = result2[0]
        bisect.insort(sorted_a, (b+1, c, result2[1]))
        print(b, result2[0])

        result3 = doit(a,c)
        intervals[(a,c)] = result3[0]
        bisect.insort(sorted_a, (a, c, result3[1]))
        print(c, result3[0])

        assert(result1[0]+result2[0]==result3[0])

#tests(10000)