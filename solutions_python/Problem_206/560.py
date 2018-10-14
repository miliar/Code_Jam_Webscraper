import datetime

def main():
    filename='A-large.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        D,N=[int(x) for x in F.readline().split()]
        Klist=[]
        Slist=[]
        Tlist=[]
        for i in range(N):
            K,S=[int(x) for x in F.readline().split()]
            Ti=(D-K)/float(S)
            Tlist.append(Ti)
        Tlist.sort()
        ans=D/Tlist[-1]
        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': '+str(ans)+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()