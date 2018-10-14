from sys import stdin

def gcd(a, b):
    return gcd(b, a%b)

for caseNo in xrange(1, int(stdin.readline())+1):
    people, up, down = [int(x) for x in stdin.readline().split()]
    players = [int(x) for x in stdin.readline().split()]
    div = -1
    for i in xrange(up, down+1):
        for p in players:
            if p%i and i%p:
                break
        else:
            div = i
            break
    if div == -1:
        print 'Case #%d: NO' % caseNo
    else:
        print 'Case #%d: %d' % (caseNo, div)
