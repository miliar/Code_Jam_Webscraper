import os

index=open("input.txt","r")
r=index.readline()
nb_case = r[0]
r=index.readline()

R=open("resultat.txt","w")
R.close()

n=1
while r!="":
    M=[]
    for line in range(0,4):
        M.append([])
        for i in range(0,len(r)-1):
            M[line].append(r[i])
        r=index.readline()
    r=index.readline()
    resultat = []
    for i in range(4):
        S=0
        for j in M[i]:
            if j=="O":
                S+=1
            if j=="X":
                S-=1
            if j=='.':
                S=0
                break
        resultat.append(S)
    for i in range(4):
        S=0
        for j in range(4):
            if M[j][i] =="O":
                S+=1
            if M[j][i]=="X":
                S-=1
            if M[j][i]=='.':
                S=0
                break
        resultat.append(S)
    S=0
    for i in range(4):
        if M[i][i] =="O":
            S+=1
        if M[i][i] =="X":
            S-=1
        if M[i][i] ==".":
            S = 0
            break
    resultat.append(S)
    S=0
    for i in range(4): 
        if M[3-i][i] =="O":
            S+=1
        if M[3-i][i] =="X":
            S-=1
        if M[3-i][i] ==".":
            S=0
            break
    resultat.append(S)

    print resultat
    completed = False
    if("." in M[0] or "." in M[1] or "." in M[2] or "." in M[3]): 
        n2=1
        for res in resultat:
            if res >=3:
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " O won" + "\n")
                completed = True
                break
            if res <=-3:
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " X won" + "\n")
                completed = True
                break

            if (completed == False and n2 == 10):
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " Game has not completed" + "\n")
                break
            n2+=1

    else:
        n2=1
        for res in resultat:
            if res >=3:
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " O won" + "\n")
                completed = True
                break
            if res <=-3:
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " X won" + "\n")
                completed = True
                break
            if (completed== False and n2 ==10):
                R=open("resultat.txt","a")
                R.write("Case #" + str(n) + ":" + " Draw" + "\n")
            n2+=1


    n=n+1
    
R.close()
