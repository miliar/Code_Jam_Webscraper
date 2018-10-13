#Jaime Marquinez

inputName='C-large.in.txt'
outputName='C-large.out.txt'

def countDeriveOfn(n,B):
    lista=[]
    nS=str(n)
    count=0
    long=len(nS)
    i=1
    while i<long:
        pot=10**i
        new=(n//pot)+(n%pot)*(10**(long-i))
        #the new in lista condition is for news that are ...
        #recycled from the same number in two differnt ways, ex: 2121 from 1212
        if n<new and new<=B and (not (new in lista)):
            lista.append(new)
            count+=1
        i+=1
    return count

def nRecycledInInterval(A,B):
    count=0
    for n in range(A,B):
        count+=countDeriveOfn(n,B)
    return count
                
def main():
    inputFile=open(inputName,'r')
    outputFile=open(outputName,'w')
    cases=int(inputFile.readline())
    count=1
    while count<=cases:
        lis=inputFile.readline().split()
        A=int(lis[0])
        B=int(lis[1])
        total=nRecycledInInterval(A,B)
        outputFile.write('Case #'+str(count)+': '+str(total)+'\n')
        count+=1
    inputFile.close()
    outputFile.close()
    print("end")
    
main()
