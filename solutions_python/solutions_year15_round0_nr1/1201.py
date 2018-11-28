import datetime

def main():
    filename='A-large.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        [Smax,aud]=F.readline().split()
        Smax=int(Smax)
        stood=0
        ans=0
        for i in range(Smax+1):
            if stood<i and int(aud[i])>0:
                ans+=i-stood
                stood=i
            stood+=int(aud[i])
            #print i,stood,ans
        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': '+str(ans)+'\n')
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    G=open('answer_'+filename,'w')
    G.writelines(answer)
    G.close()