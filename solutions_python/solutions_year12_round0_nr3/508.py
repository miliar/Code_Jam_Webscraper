'''
Created on 14.04.2012

@author: Andreas
'''

def make(minim, maxim):
    temp = []
    
    out = 0;
    for i in range(minim, maxim + 1):
        iString = str(i)
        a = len(iString)
        for j in range(1, a):
            neu = int(iString[a-j:] + iString[:a-j])
            if (len(str(neu)) != a or neu == i):
                continue
            if minim <= i <= neu <= maxim:
                abab = str(i) + " & " + str(neu)
                if not abab in temp:
                    temp.append(abab)
                    out += 1
        temp = []
    return out

filename = "D:\\codejam\\C-large.in"
out = open(filename + ".out", "w")
f = open(filename)
number = int(f.readline())
lines = f.read().splitlines()
for i in range(number):
    k = lines[i].split(' ')
    a = ("Case #" + str(i+1) + ": " + str(make(int(k[0]), int(k[1]))))
    print(a)
    out.write(a + "\n")
    