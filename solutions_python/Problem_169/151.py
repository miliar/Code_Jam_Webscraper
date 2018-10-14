import datetime

def main():
    filename='B-small-attempt2.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        olin=F.readline().split()
        N=int(olin[0])
        v=float(olin[1])
        t=float(olin[2])
        inp=[]
        for i in range(N):
            inp.append([float(x) for x in F.readline().split()])
        inp.sort(key=lambda x:x[1],reverse=True)
        if N==1:
            if t!=inp[0][1]:
                ans='IMPOSSIBLE'
            else:
                ans=str(v/inp[0][0])
        if N==2:
            if (inp[0][1]-inp[1][1])!=0:
                #X=(v*t-v*inp[1][1])/(inp[0][1]-inp[1][1])
                xx=(v*t-v*inp[1][1])
                if xx<0 or xx-v*abs(inp[0][1]-inp[1][1])>1e-10:
                    ans='IMPOSSIBLE'
                else:
                    X=v*t/(inp[0][1]-inp[1][1])-v*inp[1][1]/(inp[0][1]-inp[1][1])
                    ans=str(max(X/inp[0][0],v/inp[1][0]-X/inp[1][0]))
            else:
                if t!=inp[0][1]:
                    ans='IMPOSSIBLE'
                else:
                    ans=str(v/(inp[0][0]+inp[1][0]))

        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': '+ans+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()