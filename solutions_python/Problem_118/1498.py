def fair(i):
    s = str(i)
    for j in xrange(len(s)):
        if s[j] != s[len(s) - j - 1]:
            return False
    return True

def count(a, b):
    aa = long('1' + '0' * max(len(str(a)) / 2 - 1, 0)) 
    bb = long('1' + '0' * (len(str(b)) + 1/ 2))
    i = aa
    c = 0
    while i <= bb:
        if i % 100000 == 0:
            print i
        if fair(i):
            i_i = i * i
            if fair(i_i) and (i_i <= b) and (i_i >= a):
                c += 1
        i += 1
    return c

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        a, b = map(long, raw_input().split())
        r = count(a, b)
        print "Case #%d: %s" % (t, r)

if __name__ == '__main__':
    main()
