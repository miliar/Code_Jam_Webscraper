# Author: BAIZHIJIE (baizhj@gmail.com)

def two_gcd(a, b):
    if a==0:
        return b
    if b==0:
        return a
    c = a%b
    while c>0:
        a,b = b,c
        c = a%b
    return b
def list_gcd(a):
    a.sort()
    t = two_gcd(a[0], a[1])
    n = len(a)
    i = 2
    while i<n:
        t = two_gcd(t, a[i])
        i = i+1
    return t

def max_mod(a):
    a.sort()
    a.reverse()
    b = []
    i = 0
    la = len(a)
    while i<la-1:
        b.append(a[i]-a[i+1])
        i = i+1
    if len(b)<2:
        m = b[0]
    else:
        m = list_gcd(b)
    if m==1:
        return 0
    else:
        return (m-a[-1]%m)
    

if __name__ == '__main__':
    n = int(raw_input())
    i = 0
    while i<n:
        line = raw_input()
        line = line.split()[1:]
        line = [int(x) for x in line]
        g = list_gcd(line)
        line = [x/g for x in line]
        print 'Case #%d: %d' % (i+1, g*max_mod(line))
        i = i+1
