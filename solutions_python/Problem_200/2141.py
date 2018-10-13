
        
def solve(n):
    listN = list(str(n))
    

    if len(listN) ==1:
        return ''.join(listN)
    else:
        if isTidy(listN):
            return ''.join(listN)
        else:
            for i in range(0,len(listN)):
                

                n = n - (int(listN[len(listN)-i-1])+1)*(10**i)
                
                listN = list(str(n))
                if isTidy(listN):
                    return ''.join(listN)
    
    
    
def isTidy(listN):
    for i in range(1,len(listN)):
        if int(listN[i]) < int(listN[i-1]):
            return False
    return True


#fin = open("input.txt", "r")
#fin = open("B-small-attempt0.in","r")
fin = open("B-large.in","r")
fout = open("output.txt","w")

tFile = fin.readlines()
t = int(tFile.pop(0).strip('\n'))


for numLine in range(0,t):
    line = tFile.pop(0).strip('\n').split(' ')

    n = int(line[0])
    
    tidy = 0
    
    tidy = solve(n)
        
        

    print("Case #" + str(numLine+1) + ': ', end='')
    print("Case #" + str(numLine+1) + ': ', end='', file=fout)
    
    print(tidy)
    print(tidy, file=fout)


fout.close()
fin.close()
