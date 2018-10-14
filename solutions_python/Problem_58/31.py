from fractions import gcd

def ngame(a, b):
    if a==b:
        return False
    if a > b:
        tmp = a
        a = b
        b = tmp
    if b >= 2*a:
        return True
    else:
        return not ngame(a,b-a)

def howmany(a1,a2,b1,b2):
    i = a1
    j = b1
    count = 0
    while i<=a2:
        j=b1
        while j<=b2:
            if ngame(i,j):
                count += 1
            j+=1
        i+=1
    return count

##print howmany(1,6,1,6)
fp = open("C-small-attempt0.in", 'r')
fout = open("C-small-attempt0.out", 'w')
T = int(fp.readline())
for i in range(T):
    a1,a2,b1,b2 = fp.readline().split()
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    fout.write("Case #%d: %s\n" % (i+1, howmany(a1,a2,b1,b2) ))
fp.close()
fout.close()
