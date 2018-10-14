#!/usr/bin/python

def cnt_pal(a, b, pals):
    return len([x for x in pals if x <= b and x >= a])
    
def is_sq_palindrome(s):
    s = str(int(s)*int(s))
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]: return False
    return True

pends = tuple((str(i) for i in range(3)))

def search_pal(s, res):
    if len(s) >= 10:
            return
    for x in pends:
        #even and odd length palindromes
        p1 = (s + x) + (s+x)[::-1]
        p2 = s + x + s[::-1]
        if is_sq_palindrome(p1):
            res.add(int(p1)*int(p1))
        if is_sq_palindrome(p2):
            res.add(int(p2)*int(p2))
        search_pal(s + x, res)
    
res = set([9,])
search_pal('', res)

cases = int(raw_input())
for i in range(cases):
    s = raw_input().split()
    a, b = int(s[0]), int(s[1])
    cnt = cnt_pal(a, b, res)
    print "Case #%d: %d" % (i+1, cnt)