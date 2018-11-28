import math
import string
import re
f = open("a.in", "rU")
def gcd(a,b):
    if (a > 0) and (b > 0):
        if (a > b):
            return gcd(a-b,b)
        if (a < b):
            return gcd(a,b-a)
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b,a%b)
def ri():#int
    return int(f.readline().strip())
def rf():#float
    return float(f.readline().strip())
def rs():#string (stripped)
    return f.readline().strip()
def rl(sep=False):#list of string
    if not sep:
        return f.readline().split()
    return f.readline().split(sep)
def rli(sep=False):#list of int
    return [int(i) for i in rl(sep)]
def rlf(sep=False):#list of float
    return [float(i) for i in rl(sep)]
def rt(sep=False):#tuple of string
    return tuple(rl(sep))
def rti(sep=False):#tuple of int
    return tuple(int(i) for i in rl(sep))
def rtf(sep=False):#tuple of float
    return tuple(float(i) for i in rl(sep))



cases = ri()####
out = ""####
for case in range(cases):####
    n,x = rti()
    files = rli()
    files.sort()
    count = 0
    while (len(files) > 0) and (files[0] <= x):
        space_left = x-files[0]
        start = len(files)-1
        for i in range(start,0,-1):
            if files[i] <= space_left:
                files.remove(files[i])
                files.remove(files[0])
                count += 1
                break
            else:
                if files[i] <= x:
                    files.remove(files[i])
                    count += 1
                else:
                    files.remove(files[i])
        else:
            files.remove(files[0])
            count += 1
    out += "Case #{}: {}\n".format(case+1, count)####
f.close()####
out = out.strip()####
o = open("a.out", "w")####
o.write(out)####
o.close()####