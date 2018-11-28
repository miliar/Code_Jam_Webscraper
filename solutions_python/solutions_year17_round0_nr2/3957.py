def istidy(x):
    arr=list(str(x))
    for i in xrange(len(arr)-1):
        if int(arr[i+1])<int(arr[i]):
            return False
    return True
for cc in xrange(int(raw_input())):
    N=int(raw_input())
    while N:
        if istidy(N):
            print "Case #"+str(cc+1)+": "+str(N)
            break
        N-=1
