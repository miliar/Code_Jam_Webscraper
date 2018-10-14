T = input()

for _ in range(T):
    N = map(int,list(raw_input()))
    N.reverse()
    for i in range(len(N)-1):
        # print "i=",i," N=",N
        if N[i+1] <= N[i]:
            continue
        else:
            N[i+1]-=1
            for j in range(i+1):
                N[j]=9
    N.reverse()
    N = ''.join(map(str,N)) 
    print("Case #"+str(_+1)+": "+str(int(N)))



    # if itself tidy then itself.
    # if not - start from the back reduce by one until tidy.

    # binary search to find the tidy

