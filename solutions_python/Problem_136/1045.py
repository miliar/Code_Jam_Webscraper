def main():
    t=int(input())
    for i in range(1,t+1):
        a,b,c=map(float,raw_input().split())
        print 'Case #%d: %0.7f' % (i,call(a,b,c))
def call(c,f,x):
    cp=2
    fp=0
    mn=2<<50
    while True:
        prd_time=fp+(x/cp)
        #print prd_time
        if prd_time<mn: mn=prd_time
        elif prd_time>mn: break
        fp=fp+c/cp
        cp=cp+f
    return mn
if __name__=='__main__':
    main()
    
