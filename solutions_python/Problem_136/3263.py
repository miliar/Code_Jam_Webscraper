#Problem B
#Cookie Clicker

filename = open("B-large.in",'r')
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
filename.close()

newFile = open("output.in","w")
caseNumber = 1
for i in s[1:]:

    cps = 2.0
    ocps = 0.0

    total =  0

    C,F,X = i.split()
    C,F,X = float(C),float(F),float(X)
    c=0

    while c < X:
        
        if ocps == 0.0:
            ocps = cps
            cps += F
            c=0

        
        elif ((X/cps)+(C/ocps)) < (X/ocps):
            total += (C/ocps)
            ocps = cps
            cps += F
            c=0
        else:
            x = total
            total += (X/ocps)
            c += X
    newFile.writelines("Case #%s: "%(caseNumber),)
    newFile.writelines(str(round(total,7)))
    newFile.writelines("\n")
    caseNumber+=1

newFile.close()
