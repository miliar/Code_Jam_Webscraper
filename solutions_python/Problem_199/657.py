def flip(line,k,i):
    new_line=line[:i]
    for j in range(i,i+k):
        if line[j]=='-':
            new_line+='+'
        else:
            new_line+='-'
    new_line+=line[i+k:]
    return new_line

def flipAllPancakes(line,k):
    if not('-' in line) or len(line)==0:
        return 0
    else:
        copy=line[:]
        n=len(line)
        flips=0
        for i in range(n-k+1):
            if copy[i]=='-':
                copy=flip(copy,k,i)
                flips+=1
        if '-' in copy:
            return 'IMPOSSIBLE'
        else:
            return flips
        
def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline().split()
        pancake=case[0]
        k=int(case[1])
        fout.write('Case #'+str(i+1)+': '+str(flipAllPancakes(pancake,k))+'\n')
        
fin=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\QualRound\\1.in','r')
fout=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\QualRound\\1.out','w')
main(fin,fout)
fin.close()
fout.close()