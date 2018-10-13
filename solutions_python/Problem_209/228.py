import datetime
import math

def main(filename):
    print filename
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for qq in range(1,T+1):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        N,K=map(int,F.readline().split())
        rhlist=[]
        for i in range(N):
            [R,H]=map(int,F.readline().split())
            rhlist.append([R,2*R*H])
        rhlist.sort(key=lambda x: x[1],reverse=True)
        rhlist.sort(key=lambda x: x[0],reverse=True)
        Rmax=rhlist[0][0]
        ans=-1
        while(len(rhlist)>K-1):
            #print rhlist
            sig=rhlist[0][1]
            if K-1>0:
                Rrhlist=sorted(rhlist[1:],key=lambda x: x[1],reverse=True)
                sig+=sum ([x[1] for x in Rrhlist[:K-1]])
            ans=max(ans,math.pi*(Rmax**2+sig))
            while(len(rhlist)>0):
                if rhlist[0][0]==Rmax:
                    rhlist.pop(0)
                else:
                    Rmax=rhlist[0][0]
                    break
        
        print 'Case:%d %s:%s:%s.%s' % (qq,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(qq)+': '+str(ans)+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()




if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) > 1:
        s = args[1:]
    main(s[0])
