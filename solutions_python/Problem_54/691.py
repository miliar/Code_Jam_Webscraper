import sys
import os

os.chdir("/Users/nolze/Desktop")

fi = open("input.txt", 'r')
sys.stdin = fi

fo = open("output.txt", 'w')
sys.stdout = fo

def gcd(x, y):
    if(x == 0): return y
    return(gcd(y % x, x))


for cs in range(input()):
    l = map(int, raw_input().split())
    n = l[1:]

    if(l[0] == 2):
        sub = abs(n[0] - n[1])
        if(sub == 0):
            add = 0
        else:
            rem = min(n) % sub
            if(rem == 0): add = 0
            else: add = abs(sub - rem)
        print "Case #" + str(cs+1) + ": " + str(add)


    elif(l[0] == 3):
        sub = []
        sub.append(abs(n[0] - n[1]))
        sub.append(abs(n[1] - n[2]))
        sub.append(abs(n[2] - n[0]))
        sub.sort()

        if(sub[0] == 0):
            rem = min(n) % sub[1]
            if(rem == 0): add = 0
            else: add = abs(sub[1] - rem)
        else:
            a = gcd(sub[0], sub[1])
            b = gcd(sub[1], sub[2])
            if(a != b): a = gcd(a, b)
            rem = min(n) % a
            if(rem == 0): add = 0
            else: add = abs(a - rem)
        print "Case #" + str(cs+1) + ": " + str(add)

