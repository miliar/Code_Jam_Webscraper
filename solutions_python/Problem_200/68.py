def tidy(n):
    l = map(int, list(str(n)))
    last_raise = 0
    for i in xrange(1, len(l)):
        if l[i] < l[i-1]:
            l[last_raise] -= 1
            l[last_raise+1:] = [9]*(len(l)-last_raise-1)
            break
        if l[i] > l[i-1]:
            last_raise = i
    return int("".join(map(str, l)))

def is_tidy(n):
    l = map(int, list(str(n)))
    for i in xrange(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True

def tidy_brute(n):
    while not(is_tidy(n)):
        n -= 1
    return n

def tidy_test():
    import random
    for i in xrange(1000):
        n = random.randint(0, 10**6)
        print i, n
        assert tidy_brute(n) == tidy(n)

def main(fname):
    import os
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        n = int(in_fd.readline().strip())
        out_fd.write("Case #%d: " % (i+1) + str(tidy(n)).replace("L", "") + "\n")
    in_fd.close()
    out_fd.close()
