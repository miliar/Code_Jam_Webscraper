import sys,math

cases = int(raw_input())
inp = []




def kenAnswer(blocks, question):
    blocks.sort()
    bestIndex = 0
    for i in range(len(blocks)):
        if blocks[i] > question:
            bestIndex = i
            break
    #print "Ken played " + str(blocks[bestIndex])

    return bestIndex

def play(naomiBlocks, kenBlocks, naomiIndex):
    #print "debug play()"    
    #print naomiBlocks
    #print kenBlocks
    #print naomiIndex
    kenIndex = kenAnswer(kenBlocks,naomiBlocks[naomiIndex])

    kenMove = kenBlocks.pop(kenIndex)
    naomiMove = naomiBlocks.pop(naomiIndex)

    #print "K:" + str(kenMove) + ", N:" + str(naomiMove)
    if kenMove > naomiMove:
        #print "point to Ken"
        return 0
    else:
        #print "point to Naomi"
        return 1



def fairPlay(b1,b2):
    b1.sort()

    ken=0
    naomi=0
    for i in range(len(b1)):
        if play(b1,b2,0) == 0:
            ken+=1
        else:
            naomi+=1
    #print "Ken "+str(ken)
    #print "Naomi "+str(naomi)
    return naomi

def deceitfulPlay(b1,b2):
    b1.sort()
    b2.sort()

    epsilon = 0.000001

    

    ken=0
    naomi=0
    for i in range(len(b1)):

        maxNaomi = b1[len(b1)-1]
        maxKen = b2[len(b2)-1]

        if maxNaomi < maxKen: #losing
            naomiMove = maxKen
            
            #ken uses his max, naomi uses her min
            #print "Noemi says " +str(naomiMove) + " but plays " + str(b1[0]) 
            ken+=1
            b2.pop(len(b2)-1)
            b1.pop(0)
        else: #winning
            naomiMove = maxKen + epsilon
            #ken uses his min, naomi uses her first over his min
            naomiIndex = kenAnswer(b1,b2[0])
            #print "Noemi says " +str(naomiMove) + " but plays " + str(b1[naomiIndex]) 
            b2.pop(0)
            b1.pop(naomiIndex)
            naomi+=1



    #print "Ken "+str(ken)
    #print "Naomi "+str(naomi)
    return naomi

#input

for i in range(cases):
    raw_input() 
    list = []
    for j in range(2):
        list.append(raw_input().split(' '))
        for k in range(len(list[j])):
            list[j][k] = float(list[j][k])
    inp.append(list)

for n in range(cases):
    #print inp[n]
    #print "Fair"
    fair = fairPlay(inp[n][0][:],inp[n][1][:])
    #print "Deceitful"
    deceitful = deceitfulPlay(inp[n][0][:],inp[n][1][:])
    
    print "Case #" + str(n+1)+ ": " +str(deceitful) + " " + str(fair)

                



