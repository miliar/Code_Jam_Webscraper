f=open("sample.txt","r")
w=open("output.txt","w")

x=int(f.readline())

for tests in range(1,x+1):
    fa=[]
    sa=[]
    pcards=[]
    fr=int(f.readline())
    for i in range(0,4):
        fa.append(f.readline().strip().split(" "))
    sr=int(f.readline())
    for i in range(0,4):
        sa.append(f.readline().strip().split(" "))
    for card in fa[fr-1]:
        if card in sa[sr-1]:
            pcards.append(card)

    if len(pcards)==1:
        w.write("Case #%d: %d\n" %(tests,int(pcards[0])))
    elif len(pcards)>1:
        w.write("Case #%d: Bad magician!\n" %(tests))
    elif len(pcards)==0:
        w.write("Case #%d: Volunteer cheated!\n" %(tests))
            
f.close()
w.close()
