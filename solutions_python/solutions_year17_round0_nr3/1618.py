from heapq import heappush, heappop

def MinMax(N):
    if (N % 2) == 0:
        return N/2 - 1, N/2
    else:
        return (N-1)/2, (N-1)/2

T = raw_input()
for t in range(0, (int(T))):
    inputString = raw_input()
    inputString = inputString.split()
    N = int(inputString[0])
    K = int(inputString[1])
    i = 1
    count = [0]*(N+1)
    minS = 0
    maxS = 0
    count[N] = 1
    h = []
    heappush(h, -N)
    if N > 1000 and K > (N*0.6):
        print "Case #" + str(t+1) + ": " + str(0) + " " + str(0)
        continue
    while i <= K:
        if len(h) != 0:
            n = - heappop(h)
            count[n] -= 1
            if count[n] != 0:
                heappush(h, -n)
            minS, maxS = MinMax(n)
            if (n % 2) == 0:
                if (n/2) > 1:
                    if count[n/2] == 0:
                        heappush(h, -n/2)
                    count[n/2] += 1
                if (n/2-1) > 1:
                    if count[n/2-1] == 0:
                        heappush(h, -(n/2-1))
                    count[n/2-1] += 1
            else:
                if ((n-1)/2) > 1:
                    if count[(n-1)/2] == 0:
                        heappush(h, -(n-1)/2)
                    count[(n-1)/2] += 2
            i += 1
        else:
            minS = 0
            maxS = 0
            break
    print "Case #" + str(t+1) + ": " + str(maxS) + " " + str(minS)
