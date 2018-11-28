# -*- coding: utf-8 -*-

# QUALIFICATION ROUND 2012 - PROBLEM C
# Author: Paul Mollet-Padier

def QR2012_C():
    def gen_m(n):
        n = str(n)
        m = []
        for i in range(len(n)):
            m.append(n[i+1:] + n[:i+1])
        m.sort()
        ms = m
        for i in range(len(m)-1):
            if m[i] == m[i+1]:
                ms = m[:i] + m[i+1:]
        return ms
    
    f = open('C-small-attempt0.in')
    o = open('C-small-attempt0.out', 'w')
    
    T = int(f.readline())

    for i in range(T):
        nums = f.readline().split(' ')
        A = int(nums[0])
        B = int(nums[1])
        s = 0
        for j in range(A, B+1):
            for k in gen_m(j):
                if int(k) > j and int(k) <= B:
                    s += 1
        o.write('Case #' + str(i+1) + ': ' + str(s) + '\n')
