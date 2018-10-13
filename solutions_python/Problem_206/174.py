#!/usr/bin/python


def solve(n):
    s = list(str(n))
    peaks = [i for i in range(len(s) - 1) if s[i] > s[i+1]]
    if len(peaks) == 0:
        return n
    else:
        p = min(peaks)        
        zeros_after = len(s) - p - 1
        modulus = 10 ** zeros_after
        return n - (n % modulus) - 1

def really_solve(n):
    k = solve(n)
    if n == k:
        return n
    else:
        return really_solve(k)


def horse_time(horse, d):
    hs = horse.split()
    k = int(hs[0])
    s = int(hs[1])
    return float(d-k)/s

PATH = "/mnt/c/Users/mannes/Downloads/A-small-attempt0 (1).in"
#PATH = "test.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
inum = 0

while instances:
    params = instances[0].split()
    d = int(params[0])
    n = int(params[1])
    horses = instances[1:1+n]
    instances = instances[1+n:]
    slowest = max([horse_time(horse, d) for horse in horses])
    print "Case #{}: {}".format(inum + 1, d/slowest)
    inum += 1
