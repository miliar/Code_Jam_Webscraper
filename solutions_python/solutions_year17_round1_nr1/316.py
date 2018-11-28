import datetime

def main():
    filename='A-large.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        [R,C]=[int(x) for x in F.readline().split()]
        cake=[]
        alphlist=[]
        for i in range(R):
            cake.append([c for c in F.readline().strip()])
        
        while (1):
            countq=0
            for i in range(R):
                if cake[i].count('?')==C: # all ?
                    if i>0 and cake[i-1].count('?') != C:
                        cake[i]=cake[i-1][:]
                    elif i<R and cake[i+1].count('?') != C:
                        cake[i]=cake[i+1][:]
                    
                else:
                    for j in range(C-1):
                        if cake[i][j]=='?' and cake[i][j+1]!='?':
                            cake[i][j]=cake[i][j+1]
                    for j in range(1,C):
                        if cake[i][j]=='?' and cake[i][j-1]!='?':
                            cake[i][j]=cake[i][j-1]
                countq+=cake[i].count('?')
            if countq==0:
                break
        ans='\n'.join([''.join(cake[i]) for i in range(R)])
        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': \n'+str(ans)+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()