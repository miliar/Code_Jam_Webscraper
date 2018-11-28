#!/usr/bin/python


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def init(line):
    global s
    global n
    s = line.split(' ')
    s = [int(x) for x in s]
    n = s[0]
    s = s[1:]

def calc():
    sub = []
    for i in s:
        for j in s:
            sub.append(abs(i-j))
    ai = sub[0]
    for i in sub:
        ai = gcd(ai, i)
    return (ai - (s[0] % ai))%ai

lines = []
s = []
n = 0
ans = 0

        
lines = open("b.in").read().split('\n')

t = int(lines[0])

lines = lines[1:]

for i in range(t):
    init(lines[i])
#    for j in s:
#        print j
    ans = calc()
    print "Case #" + str(i+1) + ": " + str(ans)
