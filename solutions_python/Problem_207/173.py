from collections import Counter
import math
T = int(raw_input().strip())
for i in range(T):
    doPrint = False
    if doPrint: print "case #: ", i+1
    temp = map(int, raw_input().strip().split(" "))
    N = temp[0]
    colors = temp[1:]
    if doPrint: print "N = ", N
    if doPrint: print "colors = ", colors
    R = colors[0]
    O = colors[1]
    Y = colors[2]
    G = colors[3]
    B = colors[4]
    V = colors[5]
    
    redGroups = []
    yellowGroups = []
    blueGroups = []
    
    answer = ""
    if R < G or Y < V or B < O:
        answer = "IMPOSSIBLE"
    elif R == G and R != 0:
        if Y+V+B+O == 0:
            for j in range(R):
                answer += "RG"
        else: answer = "IMPOSSIBLE"
    elif Y == V and Y != 0:
        if R+G+B+O == 0:
            for j in range(Y):
                answer += "YV"
        else: answer = "IMPOSSIBLE"
    elif B == O and B != 0:
        if R+G+Y+V == 0:
            for j in range(B):
                answer += "BO"
        else: answer = "IMPOSSIBLE"
    else:
        firstR = "RG" * G + "R"
        firstY = "YV" * V + "Y"
        firstB = "BO" * O + "B"

#        firstR = ""
#        firstY = ""
#        firstB = ""
#        for j in range(G):
#            firstR += "RG"
#        for j in range(V):
#            firstY += "YV"
#        for j in range(O):
#            firstB += "BO"
        Rused = False
        Yused = False
        Bused = False
        
        Rgroups = [R-G, firstR] + ["R"] * (R-G-1)
#        print "Rgroups = ", Rgroups
        Ygroups = [Y-V, firstY] + ["Y"] * (Y-V-1)
        Bgroups = [B-O, firstB] + ["B"] * (B-O-1)


#        Ygroups = [Y-V, "Y", firstY]
#        Bgroups = [B-O, "B", firstB]
        groups = [Rgroups, Ygroups, Bgroups]
        if doPrint: print "groups = ", groups
        groups = sorted(groups, key=lambda x: x[0], reverse = True)
        if doPrint: print "groups (after sorted) = ", groups
        if max(Rgroups[0], Ygroups[0], Bgroups[0]) > (Rgroups[0] + Ygroups[0] + Bgroups[0]) / 2:
            answer = "IMPOSSIBLE"
        else:
            groups[0][0] -= 0.9
            answer += groups[0][1]
            del (groups[0])[1]
            while groups[0][0] + groups[1][0] + groups[2][0] > 0.5:
                tempGroups = sorted(groups[1:], key=lambda x: x[0], reverse = True)
                tempGroups.append(groups[0])
                if doPrint: print "tempGroups = ", tempGroups
                groups = tempGroups[:]
                answer += groups[0][1]
                del (groups[0])[1]
                groups[0][0] -= 1
        if doPrint: print "answer = ", answer
                
                
             
    


    if doPrint: print "answer = ", answer
        
    
    if doPrint: print " "

    if doPrint == False: print "case #" + str(i+1) + ": " + str(answer)
    