#! /usr/bin/python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def verify(val,notes,n):
    for i in range(0,n):
        if notes[i]%val!=0 and val%notes[i]!=0:
            return 0
    return 1

def solve(n,l,h,notes):
    notes.sort()
    test_lcm = 1
    possible = 0
    lcms = []
    n_lcm = 1
    for i in range(l,h+1):
        if verify(i,notes,n):
            return '%ld' % i
    return 'NO'


if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        line = f.readline().split()
        n = long(line[0])
        l = long(line[1])
        h = long(line[2])
        notes = []
        line = f.readline().split()
        for i in range(0,n):
            notes.append(long(line[i]))
        answer = solve(n,l,h,notes)
        g.write("Case #%d: %s\n" % (case,answer))
    f.close()
    g.close()