with open("sub-1.in") as f:
    t = int(f.readline().strip())
    for a in range(1,1+t):
        answer1 = int(f.readline().strip())
        for i in range(1,5):
            line = f.readline().strip().split()
            if i == answer1:
                cards1 = set(line)
        answer2 = int(f.readline().strip())
        for j in range(1,5):
            line = f.readline().strip().split()
            if j == answer2:
                cards2 = set(line)
        inboth = list(cards1.intersection(cards2))
        if len(inboth) == 1:
            print "Case #" +str(a)+":", inboth[0]
        if len(inboth) >= 2:
            print "Case #"+ str(a)+":","Bad magician!"
        if len(inboth) == 0:
            print "Case #"+str(a)+":", "Volunteer cheated!"
    #if there is only 1 card in both cards1 and cards2, then its the answer
    #if there is more than 1 card in both, then Bad Magician! (As he can't tell)
    #if 0 cards in both, Volunteer cheated!
            
    
