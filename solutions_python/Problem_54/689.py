# -*- coding: utf-8 -*-
import math
filename = "B-small-attempt3.in"

def read_C():
    f = open(filename, "r")
    T = int(f.readline().strip())
    f.close()
    return T

def convert2long_tuple(str_list):
    result = []
    for s in str_list:
        result.append(long(s))
    return tuple(result)

def read_question2(length):

    f = open(filename, "r")
    T = f.readline().strip()

    nums = []

    for i in range(length):
        n = convert2long_tuple(f.readline().strip().split(" ")[1:])
        nums.append(n)

    f.close()

    return nums

def calculate_abs(nums):
    s = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                a = abs(nums[i] - nums[j])
                s.add(a)
    l = list(s)
    l.sort()
    return l

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd_many(inputs):
    if(len(inputs)) == 1:
        #print inputs[0]
        return inputs[0]
    elif (len(inputs)) == 2:
        return gcd(inputs[0], inputs[1])
    else:
        return gcd(inputs[0], gcd_many(inputs[1:]))

outputs = []
C = read_C()
nums = read_question2(C)
for i in range(C):
    n = nums[i]
    print "n", n
    result = calculate_abs(n)
    print "result", result
    gcds = gcd_many(result)
    print "gcds", gcds
    minimum = min(n)
    if gcds == 1 or (minimum%gcds)==0:
        output=0
    else:
        output = gcds - minimum%(gcds)
    print output
    outputs.append(output)

f = open("Output1.txt", "w")
for i in range(len(outputs)):
    f.write("Case #" + str(i+1) + ": " + str(outputs[i]) + "\n")
f.close()

##
###C lines follow
##C = 3
##
##N = 3
##
##ts = (26000000,11000000,6000000)
##
###すべての差の絶対値を出す
##
###最大公約数を求める
##
###それで，一番小さい数を割って，(最大公約数-余り)が答え
##
##a = 26000000
##b = 11000000
##c = 6000000
##result = calculate_abs(a, b, c)
##gcds = gcd_many(result)
##minimum = min(a, b, c)
##print gcds - minimum%(gcds)