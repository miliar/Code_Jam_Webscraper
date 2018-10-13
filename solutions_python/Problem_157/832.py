import datetime

def getlet(a,b):
    if a==b:
        return (-1,0)
    elif (a,b)==('i','j'):
        return (1,'k')
    elif (a,b)==('j','i'):
        return (-1,'k')
    elif (a,b)==('j','k'):
        return (1,'i')
    elif (a,b)==('k','j'):
        return (-1,'i')
    elif (a,b)==('k','i'):
        return (1,'j')
    elif (a,b)==('i','k'):
        return (-1,'j')

def main():
    filename='C-small-attempt1.in'#'test.txt'#'test.txt'#'C-small-attempt0.in'
    F=open(filename,'r')
    T=int(F.readline())
    answer=[]
    for q in range(T):
        d=datetime.datetime.today()
        #read text and make answer as ans for each  question
        [n,m]=[int(x) for x in F.readline().split()]
        dstr=[c for c in F.readline().strip()*m]
        flag=0
        sflag=0
        minus=1
        ans='NO'
        while(len(dstr)>1):
            c=dstr.pop(0)
            if flag==0 and c=='i':
                flag=1
                sflag=1
            if flag==1 and c=='j':
                flag=2
                sflag=1
            if flag==2 and c=='k':
                flag=3
                sflag=1
            if not sflag:
                dd=dstr.pop(0)
                let=getlet(c,dd)
                if let[1]!=0:
                    dstr=[let[1]]+dstr
                minus=minus*let[0]
            #print dstr,flag,minus
            sflag=0
        leftover=''.join(dstr)
        if flag==2 and leftover=='k':
            flag=3
            leftover=''
        if flag==3 and leftover=='' and minus==1:
            ans= 'YES'
        else:
            ans='NO'
        print 'Case:%d %sh%sm%s.%ssecn' % (q,d.hour, d.minute, d.second, d.microsecond)
        print ans
        answer.append('Case #'+str(q+1)+': '+ans+'\n')
    F.close()
    makeanswer(filename,answer)
     
def makeanswer(filename,answer):
    F=open('answer_'+filename,'w')
    F.writelines(answer)
    F.close()