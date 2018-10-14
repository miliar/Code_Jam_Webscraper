import decimal as dc
dc.getcontext().prec = 1000
import fractions

IN = open("B-large.in", "r")
OUT = open("file.out", "w")

def compare(a, b):
    return cmp(int(a), int(b))
line = '0'
line = IN.read()

big = line.split()

counter = int(big[0])

k = 1

i = 1

while i <= counter:
    s = 'Case #' + str(i) + ':' + ' ';
    N = int(big[k])
    k = k + 1

    lst = []
    for x in range(N):
        lst.append(int(big[k]))
        k = k + 1
    
    lst.sort()

    G = lst[1] - lst[0]

    for x in range(2, N):
        G = fractions.gcd(G, lst[x] - lst[0])

    if lst[0] % G == 0:
        s = s + "0\n"
    elif 1 == 1:
        s = s + str(G - lst[0] % G) + '\n'

    OUT.write(s)
    i = i + 1
    
IN.close()
OUT.close()
print "done"
