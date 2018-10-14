import heapq

class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)

class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val


def unpack_heap(h):
    while len(h) > 0:
        yield h.heappop()

def bathroom_stalls(N, K):
    maxh = MaxHeap()
    maxh.heappush(N)
    left_block, right_block = 0, 0
    for k in range(K):
        # get largest block
        b = maxh.heappop()
        i = b//2 - (b%2 == 0)
        left_block, right_block = i, b-i-1
        if left_block > 0:
            maxh.heappush(left_block)
        if right_block > 0:
            maxh.heappush(right_block)
    # print([x for x in unpack_heap(maxh)])
    return left_block, right_block

def main():
    T = int(input())
    for t in range(1, T+1):
        n, k = [int(x) for x in input().split()]
        minLR, maxLR = bathroom_stalls(n, k)
        print("Case #%i: %i %i" % (t, maxLR, minLR))


if __name__ == '__main__':
    main()
