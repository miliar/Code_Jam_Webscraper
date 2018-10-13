filename = open("A-small-attempt0.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
cases  = int(s[0])

filename.close()
caseNumber=1
newFile = open("output.in","w")


for i in range(cases):
    newFile.writelines("Case #%s: "%(caseNumber),)
    game1Row = s[i*10+1]
    game2Row = s[i*10+6]


    x=[]
    y=1
    for j in range(i*10+2, i*10+6):
        if int(game1Row) == y:
            x = s[j]
        y+=1

    
    w=[]
    z=1
    for k in range(i*10+7, i*10+11):
        if int(game2Row) == z:
            w = s[k]
        z+=1
    xx=[]
    for n in x.split():
        xx.append(int(n))
    ww=[]
    for n in w.split():
        ww.append(int(n))

    xxx=0
    count = 0
    for n in ww:
        if n in xx:
            count+=1
            xxx=n

    if count==0:
        newFile.writelines("Volunteer cheated!")
    elif count==1:
        newFile.writelines(str(xxx))
    else:
        newFile.writelines("Bad magician!")

    newFile.writelines("\n")
    caseNumber+=1

newFile.close()
