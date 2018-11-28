def main():
    filename='A-small-attempt0.in'
    qnum=0
    T=0
    n=0
    row=[0,0]
    cand=[0,0]
    set=0
    flag=2
    answer=[]
    inputdata=open(filename,'r')
    for line in inputdata:
        line=line.strip()
        line=line.split(' ')
        line=map(int,line)
        if flag==2:
            T=line[0]
            flag=(flag+1)%2
        elif flag==1:
            set=(set+1)%2
            row[set]=line[0]
            flag=(flag+1)%2
        elif flag==0:
            n+=1
            if n==row[set]:
                cand[set]=line
            if n==4:
                if set==0:
                    qnum+=1
                    ans=magicguess(cand)
                    answer.append('Case #'+str(qnum)+': '+ans+'\n')
                    if qnum==T:
                        makeanswer(filename,answer)
                n=0
                flag=(flag+1)%2
            
        

def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()
    
def magicguess(cand):
    common=0
    commonnum=0
    for i in range(4):
        if cand[0][i] in cand[1]:
            commonnum=cand[0][i]
            common+=1
            if common==2:
                break
    if common==0:
        return 'Volunteer cheated!'
    elif common==1:
        return str(commonnum)
    elif common==2:
        return 'Bad magician!'