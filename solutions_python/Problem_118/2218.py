import math

def isPalindrome(s):
    if s[:] == s[::-1]:
        return True
    return False

def fns(fname,m):
    with open(fname) as f:
        lines = f.read().splitlines()
    n = int(lines.pop(0))
    j = 1
    # clear file
    with open('fnsans5.out', 'w') as f:
        f.write('')

    pallys = []
    # find palindromic squares:
    for i in range(1,m+1):
        if isPalindrome(str(i)):
            t = i**2
            if isPalindrome(str(t)):
                pallys.append(t)
    dromeys = set(pallys)
    for i in lines:
        a,b = i.split(' ')
        c = int(a)
        d = int(b)
        cnt = 0
        for x in dromeys:
            if x >= c and x <=d:
                cnt+=1
        with open('fnsans5.out', 'a') as f:
            f.write("Case #%d: %d\n" % (j, cnt))
        j += 1
fns("C-small-attempt3.in",1000)
