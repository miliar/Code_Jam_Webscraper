def is_tidy(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True

def tidy(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            while i < len(s) - 2 and s[i+1] == s[i+2]:
                i += 1
            return len(s) - (i+1)
    return 0

def last_tidy(n):
    while n > 0:
        t = tidy(n)
        if not t: break
        n -= 10 ** (t-1)
        s = list(str(n))
        for i in range(len(s) - t+1, len(s)):
            s[i] = '9'
        n = int(''.join(s))
    return n

T = int(input())
for i in range(T):
    n = int(input())
    d = last_tidy(n)
    if d <= n and is_tidy(d):
        print('Case #'+ str(i+1) +': ' + str(d))
    else:
        raise Exception('is not tidy '+str(n)+' '+str(d))
