import math
import heapq

sf = "C-small-1-attempt0.in"
f = open(sf, 'r')
fo = "c.out"
fout = open(fo, 'w')
T = int(f.readline())
for t in range(T):
    line = f.readline()
    splt = line.split(' ')
    N = int(splt[0])
    K = int(splt[1])
    chunks = [N]
    new_chunk_1 = new_chunk_2 = 0
    for i in range(K):
        largest = heapq.heappop(chunks)
        if largest % 2 == 1:
            new_chunk_1 = new_chunk_2 = largest / 2
        else:
            new_chunk_1 = largest / 2
            new_chunk_2 = new_chunk_1 - 1
        heapq.heappush(chunks, new_chunk_1)
        heapq.heappush(chunks, new_chunk_2)
        heapq._heapify_max(chunks)
    fout.write("Case #%d: %d %d\n" % (t + 1, new_chunk_1, new_chunk_2))
fout.close()
