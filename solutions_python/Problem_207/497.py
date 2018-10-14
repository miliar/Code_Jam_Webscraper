import datetime
import math

def findp(sukima,avd,a):
    p=0
    cavd=math.ceil(avd)
    favd=math.floor(avd)
    while(1):
        if sukima==favd*p+cavd*(a-p):    break
        else:    p+=1
#    while(1):
#        eval= avd-float(favd*p+cavd*(a-p))/a
#        if abs(eval)< 1e-5:
#            break
#        elif eval>0:
#            p=p+(a-p)/2
#        else:
#            p=p/2
    numlow=p
    numup=a-p
    return numlow,numup


def main():
    filename='B-small-attempt2.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for qqq in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        [N,R,O,Y,G,B,V]=[int(x) for x in F.readline().split()]
        #small
        clist=[[R,'R'],[Y,'Y'],[B,'B']]
        clist.sort(key=lambda x:x[0],reverse=True)
        if clist[0][0]>N/2: ans='IMPOSSIBLE'
        else:
            ans=['.']*N
            c1av=float(N-clist[0][0])/clist[0][0]
            p,q=0,0
            if (N-clist[0][0])%clist[0][0] == 0:
                p=clist[0][0]
                q=0
            else:
                p,q=findp(N-clist[0][0], c1av, clist[0][0])
            
            ans[0]=clist[0][1]
            p-=1
            ind=0
            for i in range(p):
                ans[ int(c1av)+1+ind ]=clist[0][1]
                ind+=int(c1av)+1
            for i in range(q):
                #print ans
                ans[ int(c1av)+2+ind ]=clist[0][1]
                ind+=int(c1av)+2
            for i in range(1,N):
                if ans[i]=='.' and ans[i-1]=='.':
                    ans[i-1]=clist[1][1]
                    ans[i]=  clist[2][1]
                    clist[1][0]-=1
                    clist[2][0]-=1
            for i in range(1,N-1):
                if ans[i]=='.' and ans[i-1] != ans[i+1]:
                    CC=['R','Y','B']
                    CC.remove(ans[i-1])
                    CC.remove(ans[i+1])
                    ans[i]=CC[0]
                    kk=(j for j,v in enumerate(clist) if v[0]==CC[0]).next()
                    clist[kk][0]-=1
            if ans[N-1]=='.' and ans[N-2] != ans[0]:
                CC=['R','Y','B']
                CC.remove(ans[N-2])
                CC.remove(ans[0])
                ans[N-1]=CC[0]
                kk=(j for j,v in enumerate(clist) if v[0]==CC[0]).next()
                clist[kk][0]-=1
            colind=1
            for i in range(1,N):
                if clist[colind][0]==0:
                    colind=2
                if ans[i]=='.':
                    ans[i]=clist[colind][1]
                    clist[colind][0]-=1
            ans=''.join(ans)
        


        print 'Case:%d %sh%sm%s.%ssecn' % (qqq,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(qqq+1)+': '+str(ans)+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()