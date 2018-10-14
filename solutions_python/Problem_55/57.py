#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def processFile(fname):
    def processCase(f):
        R, K, N = f.readline().strip("\n").split(" ")
        gs = f.readline().strip("\n").split(" ")
        R = int(R)
        K = int(K)
        N = int(N)
        gs = [int(g) for g in gs]
        r = 0
        k_ = 0
        k = 0
        i = j = 0
        rs = [None] * N
        while (rs[j] is None):
            print r
            while (k_ + gs[i%N] <= K):
                k_ += gs[i%N]
                i += 1
                if j == (i - N):
                    break
            rs[j%N] = (i%N, k_, r, k)
            if (r == R):
                return k
            k += k_
            r += 1
            j = i%N
            k_ = 0
        print "new"
        if (r == R+1):
            return k
        while k_ + gs[i%N] <= K:
            k_ += gs[i%N]
            i += 1
#        loop = (place, first_entered_r, f_e_k, ride_length, k_used
#        print "rs", rs[j%N]
##        print "new rs", (i%N, k_, r, k)
##        print "loop len", r - rs[j%N][2] 
##        print "loop k", k - rs[j%N][3]
##        print "loop initial k", rs[j%N][3]
##        print "loop inital r", rs[j%N][2]
##        print "loop number", j%N
#        print R, K, N, r
        l_len = r - rs[j%N][2]
        l_k = k - rs[j%N][3]
        l_i_k = rs[j%N][3]
        l_i_r = rs[j%N][2]
        l_n = j%N
#        k += k_
#        r += 1
#        print "l", l_i_k, l_i_r
        k_l = ((R - l_i_r) / (l_len) * (l_k)) + l_i_k
        r = (R - l_i_r) % l_len
        k_r = 0
        p = l_n
        while r:
            k_r += rs[p][1]
            p = rs[p][0]
            r -= 1
        return k_r + k_l
    
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

processFile("fff.in")
#processFile("sample.txt")
#processFile("C-small-attempt0.in")
#processFile("C-large.in")
