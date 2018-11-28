#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s_max,shynesses):
    ans=0
    cum=0
 
    # 0    1     .. i    ..
    # n_0  n_1   ..n_i   ..
    
    # shyness i -> (不足人数) = i - (n_0+..+n_(i-1))
    
    # count upしていく途中で、0..i-1 までに誰かいたら、その人を立たせる為に、人数の補充が
    # 行われているはずなので、それは足してしまってよい
        
    for i in range(s_max+1):
        lack = max(i-(cum+ans),0)
        cum += shynesses[i]
        ans += lack
    return ans

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        s_max,digits = raw_input().strip().split()
        shynesses=[int(digit) for digit in digits]
        print("Case #%i: %s" % (caseNr, solve(int(s_max),shynesses)))
