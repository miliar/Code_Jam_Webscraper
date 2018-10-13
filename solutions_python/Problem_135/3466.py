myInbox=open("input.txt","r")
myAnswer=open("output.txt","w")
test=int(myInbox.readline().strip("\n"))
duplicate=[]
for poop in range (test):
    duplicate=[]
    selection1=int(myInbox.readline().strip("\n"))
    party=[]
    a=[]
    b=[]
    for x in range (4):
        party.extend(myInbox.readline().strip("\n").split(" "))
    for wow in range(4):
        a.append(party[(selection1-1)*4+wow])
    selection2=int(myInbox.readline().strip("\n"))
    party=[]
    for x in range (4):
        party.extend(myInbox.readline().strip("\n").split(" "))
    for wow in range(4):
        b.append(party[(selection2-1)*4+wow])
    for i in range(4):
        if a[i] in b:
            duplicate.append(a[i])
    if len(duplicate)==0:
        myAnswer.write("Case #"+str(poop+1)+": Volunteer cheated!\n")
    elif len(duplicate)>1:
        myAnswer.write("Case #"+str(poop+1)+": Bad Magician!\n")
    else:
        myAnswer.write("Case #"+str(poop+1)+": "+("".join(duplicate))+"\n")
    print a
    print b
myAnswer.close()
myInbox.close()
