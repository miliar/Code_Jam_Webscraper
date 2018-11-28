import copy

infile = open('C-small-attempt0.in').readlines()
infile = [line.strip() for line in infile]
wfile = open('result', 'w')
T = int(infile[0])
infile = infile[1:]

def gcd_Stein(a, b):    
    if a < b:
        a, b = b, a
    if (0 == b):
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd_Stein(a/2, b/2)
    if a % 2 == 0:
        return gcd_Stein(a / 2, b)
    if b % 2 == 0:
        return gcd_Stein(a, b / 2)
    
    return gcd_Stein((a + b) / 2, (a - b) / 2) 

for case_no in range(1, T+1):
    line = infile[0]
    infile = infile[1:]
    N, L, H = [int(x) for x in line.split()]
    notes = [int(x) for x in infile[0].split()]
    infile = infile[1:]
    for i in range(L, H+1):
        thiscase = False
        thisone = True
        for j in notes:
            if i % j != 0 and j % i != 0:
                thisone = False
                break
        if thisone:
            wfile.write('Case #%d: %d\n' % (case_no, i))
            thiscase = True
            break
    if not thiscase:
        wfile.write('Case #%d: NO\n' % (case_no))
    