'''
Created on Apr 8, 2017

@author: christoph

small set version
'''

def computeLsRs(s, x):
    l = x-1
    r = x+1
    while s[l] != "0":
        l -= 1
    ls = (x - l - 1)
    while s[r] != "0":
        r += 1
    rs = (x - r + 1)*-1
    return (ls,rs)

def getMins(l):
    mins = []
    maxVal = -1
    for key, val in sorted(l.iteritems()):
        if min(val) > maxVal:
            mins = [key]
            maxVal = min(val)
        elif min(val) == maxVal:
            mins.append(key)
    return mins

def getMaxs(mins, l):
    maxs = -1
    maxVal = -1
    for i in mins:
        if max(l[i]) > maxVal:
            maxs = i
            maxVal = max(l[i])
    return maxs

def doIt(k, s):
    last = -1
    while k>0:
        l = {}
        x = 0
        while x < len(s):
            if s[x] == ".":
                l[x] = computeLsRs(s, x)
                ls = l[x][0]
                rs = l[x][1]
                while rs > 0:
                    ls += 1
                    rs -= 1
                    x += 1
                    l[x] = (ls,rs)
            x += 1
        mins = getMins(l)
        if len(mins) > 1:
            maxs = getMaxs(mins, l)
            s = s[:maxs] + "0" + s[maxs + 1:]
            last = l[maxs]
        else:
            s = s[:mins[0]] + "0" + s[mins[0]+1:]
            last = l[mins[0]]
        k -= 1
    return last

def main():
    T = int(raw_input())
    for i in range(T):
        inp = raw_input().split(" ")
        n = int(inp[0])
        k = int(inp[1])
        if (n == k):
            print "Case #" + str(i+1) + ": 0 0"
        else:
            s = "0"
            for _ in range(n):
                s += "."
            s += "0"
            out = doIt(k, s)
            print "Case #" + str(i+1) + ": " + str(max(out)) + " " + str(min(out))


if __name__ == "__main__":
    main()
