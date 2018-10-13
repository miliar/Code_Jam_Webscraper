import heapq
f = open('testfile.txt','r')
fout = open('StallOutSamll1.txt', 'w')

T = f.readline()
for iter in range(int(T)):
    input = (f.readline()).split()
    N = int(input[0])
    K = int(input[1])
    heap = []
    heapq.heappush(heap,-N)
    #could check here for some special cases such as
    #K==N where we could save some work but on input of 
    #size 10^6 the code runs in O(lgn) ~ 20 iterations
    for i in range(K):
        prev = -heapq.heappop(heap)
        max = prev/2
        min = (prev-1)/2
        heapq.heappush(heap, -max)
        heapq.heappush(heap,-min)
    fout.write("Case #{}: {} {}\n".format(iter+1,max, min))
    