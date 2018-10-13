vowel=['a','e','i','o','u']
def check(ss,n):
    c=-1
    stat=False
    p=0
    for i in range(len(ss)):
        if ss[i] not in vowel:
            p+=1
        else:
            p=0
        if p>=n:
            stat=True
            break
    return stat       
            
def allsubstrshelper(s, startindex,cou,n):
    
    #print s[startindex] 
    for i in range(startindex, len(s)): 
        #print s[startindex:i+1]
        if check(s[startindex:i+1],n):
            cou+=1
            #print s[startindex:i+1],len(s[startindex:i+1])
    return cou

def allsubstrs(s,cou,n): 
    for i in range(len(s)): 
        cou=allsubstrshelper(s, i,cou,n)
    return cou
def main():
    t=(int)(input())
    for abc in range(t):
        a,n=raw_input().split(' ')
        n=int(n)
        cou=0
        print 'Case #'+str(abc+1)+': '+str(allsubstrs(a,cou,n))
if __name__=='__main__':
    main()
