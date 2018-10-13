myfile=open("A-large.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):

    i+=1
    var=inp[i].split(" ")

    table=[]
    for q in range(int(var[0])):
        i+=1
        temp=list(inp[i])
        table.append(temp)
    for q in range(int(var[0])):
        for w in range(int(var[1])):
            if table[q][w]=="#":
                try:
                    if table[q][w+1]=="#" and table[q+1][w]=="#" and table[q+1][w+1]=="#":
                        table[q][w]="/"
                        table[q][w+1]="\\"
                        table[q+1][w]="\\"
                        table[q+1][w+1]="/"
                except:
                    pass
    for q in table:
        if "#" in q:
            answer="Impossible\n"
            break
        else:
            answer=""

    if answer!="Impossible\n":
        for q in table:
            for w in q:
                answer+=w
            answer+="\n"
    


    fullanswer+="Case #%d:\n%s" % (casenumber+1,answer)



results=open("A.out","w")
results.write(fullanswer)
myfile.close()
results.close()
