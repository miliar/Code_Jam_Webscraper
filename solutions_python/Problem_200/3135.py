def isTidy(num):
    p = 9
    while (num):
        n = num % 10
        if (n > p):
            return False
        num //= 10
        p = n
    return True


def lastTidy(N):
    if isTidy(N):
        return N

    s = list(str(N))
    l = len(s)
    for i in xrange(l-1):
        if (s[i] > s[i+1]):
            s[i] = str(int(s[i]) - 1)
            for k in xrange(i+1,l):
                s[k] = '9'
            return lastTidy(int(''.join(s)))   

    return int(''.join(s))



def main():
    n = int(raw_input())
    for x in xrange(n):
        num = int(raw_input())
        print ("Case #{}: {}").format(x+1, lastTidy(num))

if __name__ == '__main__':
    main()
