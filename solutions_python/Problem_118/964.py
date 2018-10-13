def palindrome(v):
    t = 1
    while t <= v:
        t *= 10
    t /= 10
    while t > 1:
        first = v/t
        last = v-v/10*10
        if first != last:
            return False
        v = (v-t*first)/10
        t /= 100
    return True

def fs(a, b):
    c = 0
    for i in range(int((a-.1)**.5)+1, int((b)**.5)+1):
        if palindrome(i):
            if palindrome(i**2):
                print i, i**2
                c += 1
    return c

if __name__ == '__main__':
    f = open('C-small-attempt0.in')
    o = open('C-small.out', 'w')
    n = int(f.readline())
    for i in range(n):
        a, b = [int(c) for c in f.readline().split(' ')]
        o.write('Case #%d: %d\n'%(i+1, fs(a, b)))
    o.close()
    f.close()
