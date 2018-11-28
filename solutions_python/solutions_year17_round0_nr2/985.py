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


PATH = "/mnt/c/Users/mannes/Downloads/B-small-attempt3.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
instances = [int(l) for l in instances]

for n in range(len(instances)):
    i = instances[n]
    print "Case #{}: {}".format(n + 1, really_solve(i))
