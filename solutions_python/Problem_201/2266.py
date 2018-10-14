with open('C-small-2-attempt1.in', 'r') as f:
    inputs = [line for line in f][1:]
    inputs = [(int(line.split(' ')[0]), int(line.split(' ')[1])) for line in inputs]


import heapq

def bathroom_stalls(N, K):
    q = []
    heapq.heappush(q, (-N, 1))
    while K > 0:
        N, C = heapq.heappop(q)
        N = -N
        K -= C

        if N % 2 == 0:
            heapq.heappush(q, (-(N / 2), C))
            if N / 2 > 1:
                heapq.heappush(q, (-((N / 2) - 1), C))
        else:
            heapq.heappush(q, (-(N / 2), 2 * C))

    if N % 2 == 0:
        if N / 2 > 1:
            Ls = (N / 2) - 1
        else:
            Ls = 0
        Rs = Ls + 1
    else:
        Ls = N / 2
        Rs = N / 2

    return max(Ls, Rs), min(Ls, Rs)


with open('out.txt', 'w') as f:
    for i, (N, K) in enumerate(inputs):
        ma, mi = bathroom_stalls(N, K)
        output = 'Case #{}: {} {}\n'.format(i + 1, str(ma), str(mi))
        f.write(output)
