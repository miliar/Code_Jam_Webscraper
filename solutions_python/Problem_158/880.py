f = open("C:\Users\Christofer\Documents\GCJ15\D-small-attempt1.in", "r")
fu = open("C:\Users\Christofer\Documents\GCJ15\out", "w")

t = int(f.readline())

for i in xrange(t):
    richard = True
    xrc = map(int, f.readline().split())
    x = xrc[0]
    r = xrc[1]
    c = xrc[2]
    
    if x == 1:
        richard = False
    if x == 2:
        richard = ((r*c) % 2) > 0
    if x == 3:
        richard = (((r*c) % 8) == 0 or (r == 1 or c == 1) or (r == 2 and c == 2))
    if x == 4:
        richard = (r*c) < 10
        
    if richard:
        fu.write("Case #" + str(i+1) + ": RICHARD\n")
    else:
        fu.write("Case #" + str(i+1) + ": GABRIEL\n")