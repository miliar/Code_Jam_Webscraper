



f=open("A-large.in.txt","r")
seq=f.readlines()
f.close()


N=eval(seq[0])
resultats=[]

for i in range(1,N+1):

    print("Case #"+str(i))
    l=seq[i].split()

    n=eval(l[0])

    j=1
    tabO=[]
    tabB=[]
    ordre=[]
    while j!=len(l):
        letter=l[j]
        j=j+1
        number=eval(l[j])
        j=j+1

        ordre.append(letter)
        if letter=='O':
            tabO.append(number)
        elif letter=='B':
            tabB.append(number)

    CO=1
    CB=1
    result=0

    iO=0
    iB=0

    move=0

    while move!=n:

        letter=ordre[move]

        if letter=='O':

            target=tabO[iO]

            if iB<len(tabB):
                target2=tabB[iB]

                if CB<target2:
                    CB=CB+1
                elif CB>target2:
                    CB=CB-1

            if CO<target:
                CO=CO+1
            elif CO>target:
                CO=CO-1
            else:
                iO=iO+1
                move=move+1

        if letter=='B':

           

            target=tabB[iB]

            if iO<len(tabO):
                target2=tabO[iO]
                if CO<target2:
                    CO=CO+1
                elif CO>target2:
                    CO=CO-1

            if CB<target:
                CB=CB+1
            elif CB>target:
                CB=CB-1
            else:
                iB=iB+1
                move=move+1
            

        result=result+1
        

    
                
                



    
    
    resultats.append("Case #"+str(i)+": "+str(result)+"\n")

f=open("o.in","w")
f.writelines(resultats)
f.close()

    
        
