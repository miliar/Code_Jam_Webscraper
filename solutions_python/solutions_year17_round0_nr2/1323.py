import datetime

def main():
    filename='B-large.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        S=F.readline().strip()
        n=(len(S))
        oans=1
        ans =0
        while ans!=oans:
            sans=''
            for i in range(n-1):
                if S[i]>S[i+1]:
                    sans+=str(int(S[i])-1)+'9'*(n-i-1)
                    break
                else:
                    sans+=S[i]
            else:
                sans+=S[-1]
            oans=ans
            ans=int(sans)
            S=str(ans)
            n=(len(S))
        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': '+str(ans)+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()
    
main()