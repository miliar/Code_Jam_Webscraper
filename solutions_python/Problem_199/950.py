#!/usr/bin/python

def to_bool(c):
    if c == '+':
        return True
    elif c == '-':
        return False
    else:
        assert false

def solve(s, k):

    if all(s):
        return 0
    elif len(s) < k:
        return "IMPOSSIBLE"
    elif s[0]:
        return solve(s[1:],k)
    else:
        return 1 + solve([not i for i in s[1:k]] + s[k:],k)

def really_solve(s, k):
    s = [to_bool(c) for c in s]
    try:
        return solve(s, k)
    except:
        return "IMPOSSIBLE"
        
    


PATH = "/mnt/c/Users/mannes/Downloads/A-small-attempt0.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
instances = [l.split(" ") for l in instances]

for n in range(len(instances)):
    i = instances[n]
    print "Case #{}: {}".format(n + 1, really_solve(i[0], int(i[1])))
