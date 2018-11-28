#!/usr/bin/python
#I hope this is correct, but it probably has some subtle bug...

def tostr(ar):
    s = ''
    for i in ar:
        s += str(i)
    return s

def tolist(string):
    l = list(string)
    ret = []
    for i in l:
        ret += [int(i)]
    return ret

def onesgiven(numone, numzero):
    s = tolist('1' + '0' * (numzero) + '1' * (numone - 1))
    ar = []
    while s:
        ar += [tostr(s)]
        s = lexi_next(list(s))
    return ar

def strgeneven(length):
    #four ones, three ones, two ones, one one
    ar = []
    if length >= 4:
        ar += onesgiven(4, length - 4)
    if length >= 3:
        ar += onesgiven(3, length - 3)
    if length >= 2:
        ar += onesgiven(2, length - 2)
    if length >= 1:
        ar += onesgiven(1, length - 1)
        ar += ['2' + '0' * (length - 1)]
    return [toevenpal(s) for s in ar]

def strgenodd(length):
    #max: 2 ones
    withtwo = []
    if length >= 1:
        withtwo += onesgiven(1, length - 1)
    if length >= 2:
        withtwo += onesgiven(2, length - 2)
    #max: 4 ones
    withone = withtwo[:]
    if length >= 3:
        withone += onesgiven(3, length - 3)
    if length >= 4:
        withone += onesgiven(4, length - 4)
    if length >= 1:
        withone += ['2' + '0' * (length - 1)]
    #max: 4 ones
    withzero = withone[:]
    every = [tooddpal(s, 2) for s in withtwo] + [tooddpal(s, 1) for s in withone] + [tooddpal(s, 0) for s in withzero]
    return every

def strgensingle(length):
    return ['0', '1', '2', '3']

def pallenx(x):
    if x % 2 == 0:
        return strgeneven(x/2)
    if x > 1:
        return strgenodd(x/2)
    return strgensingle(x)

#finds minimum of an array greater than bound
#assumes all elements are less than 10**53
#helper function of lexi_next
def minn(ar, bound):
    a = 10**53
    index = -1
    for i in range(len(ar)):
        if ar[i] > bound and ar[i] < a:
            a = ar[i]
            index = i
    return index

#find next lexicographic permutation of ar
#for example:
#[1, 2, 3] -> [1, 3, 2] -> [2, 1, 3] -> [2, 3, 1] -> [3, 1, 2] -> [3, 2, 1] -> None
#elements assumed to be less than 10**53
def lexi_next(ar):
    tmp = 0
    index = 0
    for i in range(len(ar) - 1, 0, -1):
        if ar[i] > ar[i-1]:
            tmp = ar[i-1]
            index = minn(ar[i:len(ar)], ar[i-1]) + i
            ar[i-1] = ar[index]
            ar[index] = tmp
            ar = ar[:i] + sorted(ar[i:])
            return ar
    return None

def reverse(s):
    return s[::-1]

def toevenpal(s):
    return int(s + reverse(s))

def tooddpal(s, n):
    return int(s + str(n) + reverse(s))

def ispal(s):
    if str(s) == reverse(str(s)):
        return True
    return False

def search(ar, item):
    maxind = len(ar) - 1
    minind = 0
    while maxind > minind:
        guess = (maxind + minind) / 2
        if ar[guess] > item:
            maxind = guess - 1
        elif ar[guess] < item:
            minind = guess + 1
        else:
            return guess
    if ar[minind] == item:
        return minind
    return minind

ar = []

for i in range(1, 52):
    ar += set([int(x)**2 for x in pallenx(i)])
ar = sorted(list(ar))#paranoia

casenum = int(raw_input())

for c in range(1, casenum + 1):
    s = raw_input()
    s = s.split()
    start = int(s[0])
    end = int(s[1])
    nar = ar[max(search(ar, start) - 5, 0): search(ar, end) + 5]#paranoia
    number = [i for i in nar if (start <= i) and (i <= end)]
    print "Case #{}: {}".format(c,len(number))
