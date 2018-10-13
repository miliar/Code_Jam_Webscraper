import math

def next_palindrome(n):
    if n < 9:
        return n + 1
    if n == 9:
        return 11
    s = str(n)
    m = len(s)
    if m & 1:
        r = m - 1
    else:
        r = m
    t = r/2
    front = s[:t]
    back = front[::-1]
    if int(back) > int(s[-t:]):
        if m & 1:
            return int(s[:t+1] + back)
        else:
            return int(s[:t] + back)
    if m & 1:
        v = (int(s[:t+1]) + 1)*(10**(m - t-1))
    else:
        v = (int(s[:t]) + 1)*(10**(m - t))
    return next_palindrome(v)

def prev_palindrome(n):
    s = str(n)
    m = len(s)
    if m & 1:
        r = m - 1
    else:
        r = m
    t = r/2
    front = s[:t]
    back = front[::-1]
    if int(back) < int(s[-t:]):
        if m & 1:
            return int(s[:t+1] + back)
        else:
            return int(s[:t] + back)
    if m & 1:
        v = (int(s[:t+1]))*(10**(m - t-1)) -1
    else:
        v = (int(s[:t]))*(10**(m - t)) - 1
    return prev_palindrome(v)


def is_palindrome(a):
    s = str(a)
    m = len(s)
    if m is 1:
        return True
    if m & 1:
        r = m - 1
    else:
        r = m
    b = r / 2
    front = int(s[:b])
    back = int(s[-b:][::-1])
    return front is back


def p3(a,b):
    counter = 0

    sqa = int(math.ceil(a**.5))
    sqb = int(math.floor(b**.5))
    i = sqa - 1
    while True:
        ii = next_palindrome(i)
        sqii = ii**2
        if sqii > b:
            return counter
        if is_palindrome(sqii):
            counter+=1
        sqrii = next_palindrome(sqii)**.5
        if sqrii > sqb:
            return counter
        if (sqrii - int(sqrii)) == 0 and is_palindrome(sqrii):
            counter+=1
        i = int(sqrii)



def main():
    with open('C-small-attempt0.in', 'r') as fn:
        n = int(fn.readline()[:-1])
        for i in range(1, n+1):
            l = fn.readline()
            if l[:-1] == '\n':
                l = l[:-1]
            f = l.split(' ')
            a = int(f[0])
            b = int(f[1])
            sln = p3(a,b)
            print 'Case #{0}: {1}'.format(i, sln)


if __name__ == '__main__':
    main()

