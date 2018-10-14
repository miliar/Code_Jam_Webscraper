# Code Jam 2017 round 1A
# MichelJ
# Problem A: Alphabet Cake

def solve(cake, r, c):
    for i in xrange(r):
        current = '?'
        for j in xrange(c):
            if cake[i][j] == '?':
                cake[i][j] = current
            else:
                current = cake[i][j]
        for j in xrange(c - 1, -1, -1):
            if cake[i][j] == '?':
                cake[i][j] = current
            else:
                current = cake[i][j]
    for j in xrange(c):
        current = '?'
        for i in xrange(r):
            if cake[i][j] == '?':
                cake[i][j] = current
            else:
                current = cake[i][j]
        for i in xrange(r - 1, -1, -1):
            if cake[i][j] == '?':
                cake[i][j] = current
            else:
                current = cake[i][j]
    return 

def main():
    for t in xrange(input()):
        r, c = map(int, raw_input().split())
        cake = [[x for x in raw_input()] for _ in xrange(r)]
        solve(cake, r, c)
        print "Case #%d:"%(t + 1)
        for row in cake:
            print "".join(row)
        
main()
