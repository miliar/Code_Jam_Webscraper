fil=open('A-small-attempt0.in','r')
noc=int(fil.readline())
i=0
p = open("rever2.in","w")
while i<noc:
    rowno1 = int(fil.readline())-1
    cardset1 = []
    for e in range(0,4):
        cardset1.append(fil.readline().split())
    rowno2 = int(fil.readline())-1
    cardset2 = []
    for e in range(0,4):
        cardset2.append(fil.readline().split())
    intersection = list(set(cardset2[rowno2]) & set(cardset1[rowno1]))
    
    if len(intersection)==1:
        p.write("Case #"+str(i+1)+": "+intersection[0]+"\n")
    elif len(intersection)>1:
        p.write("Case #"+str(i+1)+": Bad magician!\n")
    else:
        p.write("Case #"+str(i+1)+": Volunteer cheated!\n")
        
    i=i+1
p.close()
fil.close()
