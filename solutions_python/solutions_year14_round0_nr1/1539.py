f = open('A-small-attempt0.in', 'r')
num = int(f.readline())
for x in range(0, num):
    for y in range(0, 2):
        row = int(f.readline())
        for z in range (0, 4):
            if(z==row-1):
                if(y==0):
                    cards1 = f.readline().split()
                else:
                    cards2 = f.readline().split()
                    same = 0
                    for c1 in cards1:
                        for c2 in cards2:
                            if(c1==c2):
                                same+=1
                                card = c1
                    if(same==0):
                        s="Volunteer cheated!"
                    elif(same==1):
                        s=str(card)
                    else:
                        s="Bad magician!"
                    print "Case #" + str(x+1) + ": " + s
            else:
                f.readline()
    
