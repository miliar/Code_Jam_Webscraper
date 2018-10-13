import sys 
lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    x, r, c = lines[i+1].split()
    x = int(x)
    r = int(r)
    c = int(c)
    a = 1
    if x == 1 or (x == 2 and r * c % 2 == 0) or (x == 3 and r * c % 3 == 0 and r * c > 3) or (x == 4 and r * c >= 12): print 'Case #'+str(i+1)+': GABRIEL'
    else: print 'Case #'+str(i+1)+': RICHARD'
