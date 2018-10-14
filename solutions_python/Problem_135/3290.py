f=open('A-small-attempt1.in',"r")
w=open('output',"w")

cases=int(f.readline())


def readCards(f):
    cards=[]
    for i in range(4):
        line=f.readline()
        row=line.split(' ')
        for j in range(4):
            row[j]=int(row[j])
        cards.append(row)
    return cards
        
def readFile(f):
    firstAnswer=int(f.readline())
    firstArrangement=readCards(f)
    secondAnswer=int(f.readline())
    secondArrangement=readCards(f)
    return firstAnswer,secondAnswer,firstArrangement,secondArrangement

def guess(fAn,sAn,fAr,sAr):
    poss=[0 for i in range(16)]
    for i in range(4):
        poss[fAr[fAn-1][i]-1]+=1
        poss[sAr[sAn-1][i]-1]+=1
    count = 0
    for i in range(16):
        if poss[i]==2:
            count+=1
            result=i+1
    if count<1:
        return "Volunteer cheated!"
    elif count==1:
        return str(result)
    else:
        return "Bad magician!"
    
for i in range(cases):
    firstAnswer,secondAnswer,firstArrangement,secondArrangement=readFile(f)
    answer=guess(firstAnswer,secondAnswer,firstArrangement,secondArrangement)
    line= "Case #%d: %s" % (i+1,answer)
    line=line+"\n"
    #print line
    w.write(line)
w.close()
