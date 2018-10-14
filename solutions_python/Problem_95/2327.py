translateA="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
translateB="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"
translate={"q":"z", "z":"q"}
pos=0
for char in translateA:
    translate[char]=translateB[pos]
    pos+=1

firstSkipped=False
counter=1
out=open("out.txt","w")
for line in open("A-small-attempt0.in","r").readlines():
    if not firstSkipped:
        firstSkipped=True
        continue
    line=line.replace("\n","")
    newLine=""
    for char in line:
        newLine+=translate[char]
    out.write("Case #" + str(counter)+ ": " + newLine + "\n")
    counter+=1
    
out.close()