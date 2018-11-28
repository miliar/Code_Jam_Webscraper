from heapq import heappush, heappop

T = int(input().strip())
result = list()
for n in range(T):
    N, K = input().strip().split()
    N = int(N)
    K = int(K)
    heap = []
    heappush(heap, [-N,N,1])
    while K>0:
        aux, places, people = heappop(heap)
        K -= people
        L = (places-1)//2
        R = (places)//2
        inside = False
        for i in range(len(heap)):
            if heap[i][1] == L:
                heap[i][2] += (1+(L==R))*people
                inside = True
                break
        if not inside:
            heappush(heap, [-L,L, (1+(L==R))*people])
        if L != R:
            inside = False
            for i in range(len(heap)):
                if heap[i][1] == R:
                    heap[i][2] += people
                    inside = True
                    break
            if not inside:
                heappush(heap, [-R,R,people])

    print('Case #' + str(n+1)+': '+str(R)+' '+str(L))
