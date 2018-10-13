'''
Created on 8 May 2010

@author: Jirasak.Chirathivat
'''

def gcdList(diffs):
    l = len(diffs)
    g = diffs[0]
    for i in range(1, l):
        g = gcd(diffs[i], g)
    return g

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calcYears(aList):
    diffs = []
    l = len(aList)
    for i in range(1, l):
        diffs.append(abs(aList[i] - aList[i - 1]))
    g = gcdList(diffs)
    d = (aList[0] - 1) / g
    out = ((d + 1) * g) - aList[0]
    #print out, g
    return out

if __name__ == '__main__':
    readfile = file('b.in')
    lines = readfile.readlines()
    
    i = 1
    for line in lines[1:]:
        aList = [int(x) for x in line.strip().split(' ')]
        aList = aList[1:]
        value = calcYears(aList)
        print 'Case #%s: %s' % (i, value)
        i += 1 
    
    readfile.close()