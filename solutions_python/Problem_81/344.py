myfile=open("A-large.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):

    i+=1
    var=int(inp[i])
    sheet=[]

    for q in range(var):
        i+=1
        sheet.append(inp[i])
 
    data=[]
    index=0
    for q in sheet:
        games=0
        wins=0
        for w in q:
            if w=="1":
                wins+=1
                games+=1
            elif w=="0":
                games+=1

        if games!=0:
            data.append([float(wins)/float(games)])
        else:
            data.append([0])
    index=0
    for q in sheet:
        owp=0
        ucount=0
        for w in range(len(q)):

            if q[w]!=".":
                ucount+=1
                ini=w

                newword=sheet[ini]
                newword=newword[0:index]+newword[index+1:]

                games=0
                wins=0
                for e in newword:
                    if e=="1":
                        wins+=1
                        games+=1
                    elif e=="0":
                        games+=1

                if games!=0:

                    owp+=(float(wins)/float(games))

        data[index].append(owp/ucount)
        index+=1
    index=0
    for q in sheet:
        oowp=0
        count=0
        for w in range(len(q)):
            if q[w]!=".":
                count+=1
                oowp+=data[w][1]

        data[index].append(float(oowp)/count)
        index+=1
    answer=""

    for q in data:
        rpi=0.25*q[0]+0.5*q[1]+0.25*q[2]
        answer+=str(rpi)+"\n "
    
    fullanswer+="Case #%d:\n %s" % (casenumber+1,answer)



results=open("A.out","w")
results.write(fullanswer)
myfile.close()
results.close()
