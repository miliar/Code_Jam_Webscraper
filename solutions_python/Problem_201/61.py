import math

def calc_rs(n):
    if n % 2 == 0:
        return n/2
    else:
        return (n-1)/2

def calc_ls(n):
    if n % 2 == 0:
        return n/2-1
    else:
        return (n-1)/2    

def stall(n, k):
    offset = k - 1
##    print offset, n
    while offset > 0:
        if offset % 2 == 0:
            n = calc_ls(n)
            offset -= 1
        else:
            n = calc_rs(n)
        offset /= 2
##        print offset, n
    return calc_rs(n), calc_ls(n)


def comp_stalls(rs_ls0, rs_ls1):
    rs0, ls0 = rs_ls0
    rs1, ls1 = rs_ls1
    if min(rs0, ls0) < min(rs1, ls1):
        return -1
    if min(rs0, ls0) > min(rs1, ls1):
        return 1
    if max(rs0, ls0) < max(rs1, ls1):
        return -1
    if max(rs0, ls0) > max(rs1, ls1):
        return 1
    return 0
    
def stall_brute(n, k):
    stalls = [(calc_rs(n), calc_ls(n))]
    while k > 1:
        stall = stalls[-1]
        
        stalls = stalls[:-1] + [(calc_rs(stall[0]), calc_ls(stall[0])), (calc_rs(stall[1]), calc_ls(stall[1]))]
        stalls.sort(cmp=comp_stalls)
        k -= 1
    return stalls[-1]

def stall_test():
    import random
    for i in xrange(100):
        n = random.randint(1, 10**3)
        k = random.randint(1, n)
        print i, n, k
        if stall_brute(n, k) != stall(n, k):
            print  stall_brute(n, k), stall(n, k)
            assert False

def main(fname):
    import os
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        n, k = map(int, in_fd.readline().strip().split(" "))
        out_fd.write("Case #%d: " % (i+1) + " ".join(map(lambda x:str(x).replace("L", ""), stall(n, k))) + "\n")
    in_fd.close()
    out_fd.close()
