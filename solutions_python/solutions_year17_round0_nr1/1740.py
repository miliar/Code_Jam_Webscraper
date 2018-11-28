test=int(input())
inputlist=[None]*test
for i in range(test):
    counter=0
    inputstring=input()
    myarr=inputstring.split()
    nopancake=myarr[0]
    charstr=int(myarr[1])
    flipper=list(nopancake)
    for j in range(len(flipper)):
        if((j==len(flipper)-1) and (flipper[j])=='+'):
            inputlist[i]=counter
        elif((j==len(flipper)-1) and (flipper[j])=='-'):
            inputlist[i]="IMPOSSIBLE"
            break
        else:
            if(flipper[j]=='-'):
                if((len(flipper)-j+1)>charstr):
                    for k in range(j,j+charstr):
                        if flipper[k]=='+':
                            flipper[k]='-'
                        else:
                            flipper[k]='+'
                    counter=counter+1    
                    
                else:
                    inputlist[i]="IMPOSSIBLE"
                    break
    
                    
                    
for n in range(len(inputlist)):
    output="Case #"+str((n+1))
    output=str(output)+": "+str(inputlist[n])
    print(output)
