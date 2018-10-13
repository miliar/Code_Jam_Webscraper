
from time import time

start = time()

in_file = open("cs.in")

input = in_file.read().split("\n")

out_file = open("cs.out","w")


for i in range(int(input[0])):
    R, k, N = input[2 * i + 1].split(" ")
    R, k, N = int(R), int(k), int(N)
    
    g = input[2 * i + 2].split(" ")
    for j in range(N):
        g[j] = int(g[j])
    
    pos = 0
    win = 0
    
    cache = {}
    
    r = 0
    while r < R:
        kl = k 
        s, e = pos, pos-1
        while kl >= g[pos]:
            if s <= pos <= e:
                break
            e = pos
            kl -= g[pos]
            win += g[pos]
            pos += 1
            if pos is N:
                pos = 0
        r += 1
        if pos in cache:
            # gewinn bis zum cache, rides bis zum cache
            w, rn = cache[pos]
            
            # noch uebrige rides
            rl = R - r
            
            if rl is 0:
                break
            #print "rl", rl
            # rides die durch den cache zu machen sind
            d = rl / (r - rn)
            dr = d * (r - rn)
            #print "d", d, dr
            # gewinn seit cache eintrag
            wj = win - w
            #print "wj", wj
            
            win += wj * d
            r += dr
            
            
            
        else:
            cache.update({pos:(win, r)})
        
    print "Case #" + str(i + 1) + ": " + str(win)
    out_file.write("Case #" + str(i + 1) + ": " + str(win) + "\n")
    
    print "Used time: " + str(time() - start)
    #print cache
    """
    if n % 2**k == 0:
        
    else: 
        out_file.write("Case #" + str(i+1) + ": OFF\n")
    """
out_file.close()
