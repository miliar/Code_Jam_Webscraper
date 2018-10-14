def list_int():
    m=raw_input()
    m=m.split()
    m= map(float,m)
    return sorted(m,reverse=True)
def compare(a,b):
    if(a>b):
        return 1
    else :
        return -1
def getScore(a1,a2):
    i=0
    j=0
    score=0
    while(i<len(a1) and j< len(a2)):
        val=a1[i]
        val2=a2[j]
        if(compare(val,val2)>0):
            i+=1
            score+=1
        j+=1
    return score





def main():
    t=int(input())
    for i in range(t):
        y=0
        x=0
        n=int(input())
        if n==1 :
            naomi=float (input())
            ken= float(input())
            if ( ken > naomi):
                x=0
                y=0
            else:
                x=1
                y=1

        else:
            naomi=list_int()

            ken=list_int()
            #print naomi,ken
            scoreD=getScore(naomi,ken)
            scoreW=n-getScore(ken,naomi)
            x=scoreD
            y=scoreW

        print 'Case #'+str(i+1)+': '+ str(x)+' '+str(y)








main()


