def findTidy(numstr):
    n=len(numstr)
    if n==1:
        return numstr
    else:
        i=0
        terminate=False
        newstr=''
        while i<n-1 and not(terminate):
            if numstr[i]>numstr[i+1]:
                newstr=numstr[:i]+str(int(numstr[i])-1)+(n-i-1)*'9'
                for j in range(i-1,-1,-1):
                    if newstr[j]>newstr[j+1]:
                        newstr=newstr[:j]+str(int(newstr[j])-1)+(n-j-1)*'9'
                terminate=True
            i+=1
        if terminate==False:
            newstr=numstr 
        if newstr[0]=='0':
            newstr=newstr[1:]
        return newstr    

def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline()
        case=case[:-1]
        fout.write('Case #'+str(i+1)+': '+findTidy(case)+'\n')

fin=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\QualRound\\2.in','r')
fout=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\QualRound\\2.out','w')
main(fin,fout)
fin.close()
fout.close()