
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of string, int
    
    runs = [0]*n
    runs[-1]=1
    largestPointer = n-1

    for j in range(k):
        while(runs[largestPointer]==0):
            largestPointer-=1
        biggest = largestPointer+1
        L = (biggest-1)/2
        R = biggest-L-1
        if(L>0):
            runs[L-1]+=1
        if(R>0):
            runs[R-1]+=1
        runs[largestPointer]-=1


    print "Case #" +str(i)+": " + str(max(L,R)) + " " + str(min(L,R))

