import datetime
import bisect

def main():
    filename='C-small-2-attempt1.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        n,k=[int(x) for x in F.readline().split()]
        fib=[2**i-1 for i in range(1,20)]
        a=n-1
        if k>1:
            m=bisect.bisect_left(fib,k)
            t=(n-fib[m-1])/2**m
            s=(n-fib[m-1])%2**m
            if k<=fib[m-1]+s:    a=t
            else:                a=t-1
        ans=' '.join([str(x) for x in ([a-a/2,a/2])])
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