file = open("A-small-attempt0.in","r")
outfile=open("outl.txt","w")
t_case=file.readline()
def settle(r1,l1,r2,l2):
    row1=l1[r1-1]
    row2=l2[r2-1]
    final=[]
    for x in row1:
        for y in row2:
            if int(x)==int(y):
                final.append(x)
    return final
for k in range(0,int(t_case)):
    r1=int(file.readline())
    list1=[]
    for x in range(0,4):
        list1.append(file.readline().split())
    r2=int(file.readline())
    list2=[]
    for y in range(0,4):
        list2.append(file.readline().split())
    listo=settle(r1,list1,r2,list2)
    out="Case #"+str(k+1)+": "
    if len(listo)>1:
        out+= "Bad magician!"
    elif len(listo)<1:
        out+= "Volunteer cheated!"
    else:
        out+=listo[0]
    outfile.write(out+"\n")
    print(out)
