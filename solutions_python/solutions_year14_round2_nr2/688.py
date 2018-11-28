def toBinary(n):
    return "{0:b}".format(n)

def bitwiseAND(a, b):
    a = toBinary(a)
    b = toBinary(b)

    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    else:
        a = '0' * (len(b) - len(a)) + a

    n = len(a)

    new = ''
    for i in range(n):
        if a[i] == '1' and a[i] == b[i]:
            new += '1'
        else:
            new += '0'

    return new

f = open('B-small-attempt0.in', 'r')
o = open('B-small-attempt0.out', 'w')

T = int(f.readline())

for t in range(T):
    line = map(int, f.readline().split())
    A = line[0]
    B = line[1]
    K = line[2]

    counter = 0
    for a in range(A):
        for b in range(B):
            if int(bitwiseAND(a, b), 2) < K:
                counter +=1

    o.write("Case #%d: %s\n" %(t+1, counter))