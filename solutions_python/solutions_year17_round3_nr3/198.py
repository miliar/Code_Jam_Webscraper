import datetime

def main(filename):
    print filename
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for qq in range(1,T+1):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        [N,K]=map(int,F.readline().split())
        U=float(F.readline())
        P=map(float,F.readline().split())
        #N==K
        P.sort()
        Pdict={1.000: 1}
        for p in P:
            if p not in Pdict.keys():
                Pdict[p]=1
            else:
                Pdict[p]+=1
        Pkeys=sorted(Pdict.keys())
        while(U>1e-6):
            smallest=Pkeys[0]
            nextsmallest=Pkeys[1]
            if (nextsmallest-smallest)*Pdict[smallest]<=U:
                U-=(nextsmallest-smallest)*Pdict[smallest]
                Pdict[nextsmallest]+=Pdict[smallest]
                Pdict[smallest]=0
                del Pkeys[0]
            else:
                nd=Pdict[smallest]
                Pdict[smallest+U/nd]=Pdict[smallest]
                Pkeys.append(smallest+U/nd)
                del Pkeys[0]
                Pdict[smallest]=0
                U=0
                break
        ans=1
        for p in Pkeys:
            ans*=p**Pdict[p]
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
