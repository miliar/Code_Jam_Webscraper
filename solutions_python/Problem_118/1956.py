import math

def palindrome(num):
    check=list(str(num))
    retorno=True
    for i in range(0,len(check)):
        if check[i]!=check[len(check)-i-1]:
            retorno=False
    return retorno

def isSquare(num):
    res=math.sqrt(num)
    lnro=list(str(res).split("."))
    if lnro[1]=="0":
        return int(lnro[0])
    else:
        return -1

def output(status,caseNumber):
    fout=open("output.txt","a")
    fout.write("Case #"+str(caseNumber)+": "+str(status)+"\n")
    fout.close()

f=open("C-small-attempt0.in","r")
f.readline()
isEOF=False
case=1
while isEOF==False:
    lRan=[]
    ran=f.readline()
    if not ran:
        isEOF=True
    else:
        ran.strip()
        lRan=ran.split(" ")
        counter=0
        for i in range(int(lRan[0]),int(lRan[1])+1):
            if palindrome(i)==True:
                esCuad=isSquare(i)
                if esCuad!=-1:
                    if palindrome(esCuad)==True:

                        counter=counter+1
        output(counter,case)
        case=case+1
f.close()