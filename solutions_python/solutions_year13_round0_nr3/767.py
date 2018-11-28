__author__ = 'darinflar'

def isPalindrome(s):
    assert isinstance(s, str)
    return s == "".join([i for i in reversed(s)])

def isCool(a):
    return isPalindrome(str(a)) and isPalindrome(str(a ** 2))

a = []

def upperBound(v):
    global a
    l, r = -1, len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] > v:
            r = m
        else:
            l = m
    return r

def lowerBound(v):
    global a
    l, r = -1, len(a)
    while r - l > 1:
        m = (l + r) // 2
        if a[m] >= v:
            r = m
        else:
            l = m
    return r

def run():
    l, r = map(int, input().split())
    l, r = lowerBound(l), upperBound(r)
    return max(0, r - l)

def add(s):
    global a
    assert (len(s) > 0 and s[0] != '0')
    if isCool(int(s)):
        a += [int(s) ** 2]

cc = 10

def make(s = ""):
    assert isinstance(s, str)
    if 0 < len(s) <= cc:
        add(s)
    if len(s) > cc:
        return ;
    if s != "":
        make(s + "0")
    make(s + "1")
    make(s + "2")

a += [9]
make()
a.sort()
#for i in a:
#    print ("(%d -> %d)"%(i, i ** 2))
#print (a)
t = int(input())
for i in range(t):
    print ("Case #%d: %d"%(i + 1, run()))