def checkit(str):
    p=0
    while p+n<=l:
        if len(str[p:p+n])==n and snd(str[p:p+n]):
            return len(str)-n-p+1
        p+=1
    return 0


def snd(str):
    #print str
    v=0
    for k in range(len(str)):
        if str[k] in vo: v=1
    if v==1: return False
    return True


T = int(raw_input())
vo=['a','e','i','o','u']
for testcase in range(1, T+1):
    a, n = raw_input().split()
    cnt,l,n=0,len(a),int(n)
    for i in range(l-n+1):
        cnt+=checkit(a[i:])
        #print cnt
    print "Case #%d: %d" % (testcase, cnt)
        