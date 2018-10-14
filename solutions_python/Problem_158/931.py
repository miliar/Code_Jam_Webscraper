#from sys import stdin as inp
inp = file('D-small-attempt1.in', 'r')
out = file('D-small-attempt1.out', 'w')
t = int(inp.readline())
for case in xrange(1, t+1):
    x, r, c = map(int, inp.readline().split())
    ans = 'RICHARD'
    if x == 1:
        ans = 'GABRIEL'
    elif x<7 and (r*c)%x == 0 and (r>=x or c>=x):
        if x == 2:
            ans = 'GABRIEL'
        elif x==3 and r>1 and c>1:
            ans = 'GABRIEL'
        elif x == 4 and r> 2 and c>2:
            ans = 'GABRIEL'
    out.write('Case #%d: %s\n'%(case, ans))
out.close()
inp.close()
