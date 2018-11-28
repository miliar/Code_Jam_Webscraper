import sys
def func():
    op = open(sys.argv[2],'a')
    global time,ans,start
    while(ans):
        if(time+X/start <= (time+C/start+X/(start+F))):
            time+=X/start
            op.write( 'Case #%d: %.7f\n' % (case,time))
            print 'Case #%d: %.7f\n' % (case,time)
            ans = False
        else:
            time+=C/start
            start+=F
    op.close()

f = open(sys.argv[1])
cases = int(f.readline())
print cases
case = 1
start = 2.0
time = 0.0
ans = True
while cases:
    s = f.readline().split()
    print s
    C,F,X = float(s[0]),float(s[1]),float(s[2])
    func()
    cases-=1
    case+=1
    s = []
    C=0.0
    F=0.0
    X=0.0
    time =0.0
    start =2.0
    ans = True
f.close()
