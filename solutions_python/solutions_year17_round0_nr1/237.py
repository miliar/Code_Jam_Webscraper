# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# nb tests
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    ins,K=raw_input().split(" ")
    K=int(K)
    N=len(ins)
    sig=[1]*N
    strbase=[1 if k=="+" else -1 for k in ins]
    res=0
    for j in range(N):
     #    print i, strbase[i]*sig[i]
        if strbase[j]*sig[j]==-1:
            if j>N-K:
                res="IMPOSSIBLE"
                break
            res+=1
            for k in range(K):
                sig[j+k]*=-1

    print "Case #{}: {}".format(i,res)
