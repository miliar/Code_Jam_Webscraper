def tidyN(num):
    N = str(num)
    tidy = False
    val=""
    
    if len(N) == 1:
        val=N[0]
        tidy = True
    if tidy == False:
        val+=str(N[0])
        for i in range(0,len(N)-1):
            if int(N[i]) <= int(N[i+1]):
                val+=str(N[i+1])
                tidy = True
            else:
                val+=str(N[i+1])
                val=str(int(val)-1)
                for j in range(i+2, len(N)):
                    val+="9"
                tidy = False
                break
                
    if tidy == False:
        return tidyN(val)
    else:
        return val

f = open("B-large.in","r")
g = open("ans.txt", "w")

maxCase = f.readline()
Case = 1

for line in f:
    N = line.rstrip("\n")
    
    val = tidyN(N)

    g.write("Case #"+ str(Case) + ": " + val + "\n")
    Case += 1
        
f.close()
g.close()
    