def findTidy(p):
    s = str(p)
    n = len(s)
    l = s[0]
    for i in range(1,len(s)):
        c = s[i]
        if c < l:
            b = p % 10**(n - i)
            return p - b - 1
        l = c
    return p

def recFind(p):
    x = p
    y = findTidy(p)
    while y != x:
        x = y
        y = findTidy(y)
    return y

def main():
    n = int(raw_input())
    a = []
    for i in range(n):
        a.append(int(raw_input()))
    for i in range(len(a)):
        print "Case #%d: %d" %(i+1, recFind(a[i]))

if __name__ == "__main__":
    main()