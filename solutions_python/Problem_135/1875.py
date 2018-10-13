f=open("A-small-attempt0.in", "r")
bad="Bad magician!"
cheat="Volunteer cheated!"
listeResults=[]
listeRaw1=[]
listeRaw2=[]
nbTest = int(f.readline())
i=0
raw1=100
raw2=100
for ligne in f:
    if i==0:
        raw1=int(ligne)
    if i==5:
        raw2=int(ligne)
    if raw1==i:
        listeRaw1=ligne.rstrip('\n\r').split(" ")
    if raw2+5==i:
        listeRaw2=ligne.rstrip('\n\r').split(" ")
    i+=1
    if i==10:
        same=0
        num=0
        for k in range (len(listeRaw1)):
            for kk in range (len(listeRaw2)):
                if listeRaw1[k]==listeRaw2[kk]:
                    same+=1
                    num=listeRaw1[k]
        if same == 0:
            listeResults.append(cheat)
        if same == 1:
            listeResults.append(num)
        if same > 1:
            listeResults.append(bad)
        i=0
        listeRaw1=[]
        listeRaw2=[]

f.close()
f=open("Output.txt", "w")
z=0
while z < nbTest:
    print("Case #"+ str(z+1)+": "+listeResults[z]+'\n')
    f.write("Case #"+ str(z+1)+": "+listeResults[z]+'\n')

    z+=1
f.close()
