#!python
#-*- encoding:utf-8 -*-
import math
import sys

def isPalindrome(num):
    num_s = str(num)
    begin = 0
    end = len(num_s) - 1
    while(begin <= end):
        if(num_s[begin] != num_s[end]):
            return False
        begin += 1;
        end -= 1;
    return True

def solve(list, pl):
    return len(filter(lambda x: list[0] <= x <= list[1], pl))

if __name__ == "__main__":
    inp = open(sys.argv[1],  "r")
    out = open(sys.argv[1]+".out", "w")

    testcase = int(inp.readline()[:-1])

    cases = [map(lambda x: int(x), inp.readline()[:-1].split(" "))
             for i in range(testcase)]
    inp.close()

    l = range(1, int(math.sqrt(10**14)+1))
    l = filter(isPalindrome, l)
    l = map(lambda x: x**2, l)
    l = filter(isPalindrome, l)
    for i in range(testcase):
        out.write("Case #%d: %d\n" % (i+1, solve(cases[i], l)))
        #print("Case #%d: %d" % (i+1, solve(cases[i], l)))

    out.close()
