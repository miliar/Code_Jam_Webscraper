#!/usr/bin/env python

def isitfair(anumb):
    if len(str(anumb)) == 1:
        return 1
    elif len(str(anumb)) == 2 or len(str(anumb)) == 3:
        if str(anumb)[0] == str(anumb)[len(str(anumb)) - 1]:
            return 1
        else: return 0
    else:
        if str(anumb)[0] == str(anumb)[3] and str(anumb)[1] == str(anumb)[2]:
            return 1
        else: return 0

def isitsquare(bnumb):
    sqrt = bnumb**(0.5)
    if sqrt/int(sqrt) != 1:
        return 0
    else: return 1

if __name__ == "__main__":
    f = open('a.in', 'r')
    T = int(f.readline())
    for a in range(1, T+1):
        result = 0
        mini,maxi = f.readline().split()
        for number in range(int(mini),int(maxi)+1):
            if isitfair(number) and isitsquare(number) and isitfair(int(number**(0.5))):
                result += 1
        print "Case #" + str(a) + ":", str(result)