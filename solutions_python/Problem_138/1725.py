# Qualification Round
# Problem D

fname = "D-large.in"
f = open(fname,"r")

T = int(f.readline())
for case in range(1,T+1):
    N = int(f.readline())
    blocksNaomi = map(float, f.readline().split())
    blocksKen = map(float, f.readline().split())
    blocksKen.sort()
    kencopy = blocksKen[:]
    
    # Normal War
    points1 = 0
    for mass in blocksNaomi:
        if blocksKen[-1] < mass:
            points1 += 1
            blocksKen.pop(0)
        else:
            for i,b in enumerate(blocksKen):
                if b > mass:
                    blocksKen.pop(i)
                    break
#        print mass, blocksKen
    
    # Deceitful War
    blocksNaomi.sort()
    blocksKen = kencopy[:]
    points2 = 0
    for k in range(N):
        # see if we can cheat
        canCheat = False
        for idx,mass in enumerate(blocksNaomi):
            if mass > blocksKen[0]:
                points2 += 1
#                print "Play:",mass," vs ", blocksKen[0]
                blocksNaomi.pop(idx)
                blocksKen.pop(0)
                canCheat = True
                break             

    print "Case #%i: %i %i" % (case,points2,points1)

        