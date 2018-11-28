import os
import heapq

input_file = 'C-mid.in'
out_file = input_file.replace('.in', '.out')
data = os.path.join(os.path.dirname(__file__), input_file)
data_o = os.path.join(os.path.dirname(__file__), out_file)

with open(data, 'r') as f:
    with open(data_o, 'w+') as ff:
        T = int(f.readline().strip('\n'))
        for case in range(1, T + 1):
            n, k = [int(it) for it in f.readline().strip('\n').split()]
            heap = []
            heapq.heappush(heap, -n)
            for _ in range(k):
                v = -heapq.heappop(heap)
                m, M = int(v / 2), int((v - 1) / 2)
                heapq.heappush(heap, -m)
                heapq.heappush(heap, -M)
            ff.write('Case #%i: %s %s\n' % (case, m, M))
