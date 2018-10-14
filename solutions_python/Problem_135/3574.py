c=int(raw_input())
dev=""
for i in range(c):
    f=int(raw_input())-1
    filas=[]
    for x in range(4):
        filas.append(raw_input())
    fila=filas[f]
    nums1=fila.split(" ")
    f=int(raw_input())-1
    filas=[]
    for x in range(4):
        filas.append(raw_input())
    fila=filas[f]
    nums2=fila.split(" ")
    si=False
    guardo=[]
    for n in nums1:
        if n in nums2:
            guardo.append(n)
    if len(guardo)==1:
        dev+="Case #"+str(i+1)+": "+str(guardo[0])+"\n"
    elif len(guardo)>1:
        dev+="Case #"+str(i+1)+": Bad magician!\n"
    else:
        dev+="Case #"+str(i+1)+": Volunteer cheated!\n"
print dev