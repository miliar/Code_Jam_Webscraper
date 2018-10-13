for TC in range(1, input()+1):
    size, n = map(int, raw_input().split())
    motes = sorted(map(int, raw_input().split()))
    
    if size == 1:
        print "Case #%d: %d" % (TC, n)
        continue
        
    changes = 0
    for i, mote in enumerate(motes):
        if size > mote: # if bigger, eat
            size += mote
        else:
            if i == n-1: # if last mote, just delete it
                changes += 1
            else:
                tempsize = size
                tempchange = 0
                while tempsize <= mote:
                    tempsize += tempsize - 1
                    tempchange += 1
                if tempchange >= n-i:
                    changes += n-i # delete remaining mote
                    break
                else: # eat current and intermediate motes
                    size = tempsize + mote
                    changes += tempchange
    print "Case #%d: %d" % (TC, changes)