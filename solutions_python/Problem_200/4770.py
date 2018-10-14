t = int(input())
f = open('output.txt','w')
for test in range (t):
    n = int(input())
    chislo = list(str(n))
    for i in range (len(chislo)-1,0,-1):
        if int(chislo[i])==0:
            chislo[i]=9
            for j in range (i-1,-1,-1):
                if chislo[i]>int(chislo[j]) and chislo[j]!='0':
                    chislo[j]=int(chislo[j])-1
                    break

                else:
                    chislo[j]=chislo[i]
            for k in range (len(chislo)-1,i,-1):
                chislo[k]=9
        elif int(chislo[i])>= int(chislo[i-1]):
            chislo[i]=int(chislo[i])
        elif int(chislo[i])< int(chislo[i-1]):
            chislo[i-1]=int(chislo[i-1])-1
            for j in range (len(chislo)-1,i-1,-1):
                chislo[j]=9
    number = str()
    for i in range (len(chislo)):
        if i==0 and chislo[i]==0:
            pass
        else:
            number = number+str(chislo[i])
    number='Case #'+str(test+1)+': '+number+'\n'
    f.write(number)