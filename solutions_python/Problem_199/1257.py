import datetime

def main():
    filename='A-large.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        s=F.readline().split()
        k=int(s[1])
        p=[0 if i=='-' else 1 for i in s[0]]
        lp=len(p)
        ans=0
        for i in range(lp-(k-1)):
            if not p[i]:
                ans+=1
                p[i:i+k]=[not j for j in p[i:i+k]]
        if 0 in p:
            ans='IMPOSSIBLE'
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