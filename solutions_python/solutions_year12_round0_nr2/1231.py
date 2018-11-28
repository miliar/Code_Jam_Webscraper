
file = open("cockfarthuge.txt")

asscock = 0

for line in file:
    if asscock == 0:
        asscock += 1
        continue
    yes = 0
    no = 0
    maybe = 0
    nums = line.split(" ")
    del(nums[0])
    surprises = int(nums[0])
    thresh = int(nums[1])
    del(nums[0])
    del(nums[0])
    for n in nums:
        score = int(n)
        loki1 = score/3.
        if (loki1 % 1) == 0:
            loki2 = loki1
            loki3 = loki1
            best = loki1 + 1
        else:
            loki1 = int(loki1)
            loki2 = (score-loki1)/2.
            if (loki2 % 1) == 0:
                loki3 = loki2
                best = loki2 + 1
            else:
                loki2 = int(loki2)
                loki3 = score - (loki1 + loki2)
                best = max([loki1,loki2,loki3])
        m = [loki1,loki2,loki3]
        m = max(m)
        if m == 0:
            best = 0
        if m >= thresh:
            yes += 1
            continue
        elif best >= thresh:
            maybe += 1
            continue
        else:
            no += 1
            continue
    winners = yes
    if maybe < surprises:
        winners += maybe
    elif maybe >= surprises:
        winners += surprises
    print "Case #" + str(asscock) + ": " + str(winners)
    asscock += 1
            
                
