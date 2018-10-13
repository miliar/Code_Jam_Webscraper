#! /usr/bin/python

def gcd(a, b):
        if a*b == 0:
                return a + b
        elif a == b:
                return a
        else:
                return gcd(a%b, b%a)

f = open('B-large.in', 'r')
f1 = open('output.out', 'w')
s = f.readline()
c = int(s)

for i in range(c):
        s = f.readline()
        l = s.split(' ')
        N = int(l[0])
        g = abs(int(l[2]) - int(l[1]));
        for j in range(1, N+1):
                for k in range(j+1, N+1):
                        g = gcd(g, abs(int(l[j]) - int(l[k])))
        f1.write("Case #" + str(i + 1) + ": " + str((-int(l[1]))%g) + "\n")
