import numpy as np

def main():
    filename='B-large.in'
    flag=1
    T=0
    qnum=0
    answer=[]
    inputdata=open(filename,'r')
    for line in inputdata:
        line=line.strip()
        line=line.split(' ')
        line=map(float,line)
        if flag==1:
            T=line[0]
            flag=0
        else:
            qnum+=1
            ans=getbesttime(line)
            answer.append('Case #'+str(qnum)+': '+"%0.7f"%(ans)+'\n')
            if qnum==T:
                makeanswer(filename,answer)
                
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()

def getbesttime(line):
    C,F,X=line
    buy=True
    n=2
    time=0
    while buy:
        buy=((C/n)+(X/(n+F)))<(X/n)
        if buy:
            time+=(C/n)
        else:
            time+=X/n
        n+=F
    return time