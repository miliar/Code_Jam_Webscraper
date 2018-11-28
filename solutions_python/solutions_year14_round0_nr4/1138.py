txtFile="input.txt"
txt_file = open(txtFile);

#x=int(input())
lst=[]
for line in txt_file.readlines():
    #z=input()
    a=line.strip(" ").split()
    b=[]
    for d in range(len(a)):
        b.append(float(a.pop(0)))
    
    b.sort()
    b.reverse()
    #print(b)
    lst.append(b)
x=lst.pop(0).pop()
#print(lst)


output_file = open("output.txt", "w")
case=1
index=0
while index<len(lst):
    real=0
    cheat=0
    naomi=[]
    ken=[]
    for x in range(len(lst[index+1])):
        n=lst[index+1][0]
        if n>lst[index+2][0]:
            
            if n>lst[index+2][len(lst[index+2])-1]:
                
                real+=1
                h=lst[index+1].pop(0)
                #print(h)
                l=lst[index+2].pop(len(lst[index+2])-1)
                #print(l)
                naomi.append(h)
                ken.append(l)
        else:
            h=lst[index+1].pop(0)
            l=lst[index+2].pop(0)
            naomi.append(h)
            ken.append(l)
    #print(naomi)
    #print(ken)
    naomi.sort()
    #naomi.reverse()
    ken.sort()
    #ken.reverse()
    #print(naomi)
    #print(ken)
    #print(lst)
    while len(naomi)!=0:
        f=naomi.pop(0)
        if f<ken[0]:
            s=ken.pop(len(ken)-1)
        else:
            s=ken.pop(0)
            cheat+=1
    
    index+=3
    output_file.write("Case #")
    output_file.write(str(case))
    output_file.write(": ")
    output_file.write(str(cheat))
    output_file.write(" ")
    output_file.write(str(real))
    #print("cheat "+str(cheat))
    #print("real "+str(real))
    case+=1
    output_file.write("\n")
output_file.close()

