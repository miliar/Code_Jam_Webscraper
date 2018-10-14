import math
import heapq
from collections import defaultdict

def compute(spots, fills):
    empties = spots - fills
    interval = fills + 1

    q = float(empties) / interval
    ceil = math.ceil(q)
    floor = math.floor(q)
    return int(ceil), int(floor)

def compute2(spots, fills):
    heap = [spots]
    l, r = 0, 0
    for i in xrange(fills):
        t = heap.pop(0)
        t  -=  1
        l, r = int(math.ceil(float(t)/2)), int(math.floor(float(t)/2))
        if 0 < l:
            heap.append(l)
        if 0 < r:
            heap.append(r)
        heapq._heapify_max(heap)
    left, right = max(l, r), min(l, r)
    return left, right

def compute3(spots, fills):
    heap = [spots]
    l, r = 0, 0
    for i in xrange(fills):
        curr = heap.pop(0)
        curr  -=  1
        if curr < 2:
            continue
        l, r = int(math.ceil(float(curr)/2)), int(math.floor(float(curr)/2))
        if 0 < l:
            heap.append(l)
        if 0 < r:
            heap.append(r)
        heapq._heapify_max(heap)
    left, right = max(l, r), min(l, r)
    return left, right

def compute4(spots, fills):
    dheap = defaultdict(int)
    dheap[spots] = 1
    curr = spots
    l, r = 0, 0
    for i in xrange(fills):
        dheap[curr] -= 1
        curr  -=  1
        if curr < 0:
            return 0, 0
        l, r = int(math.ceil(float(curr)/2)), int(math.floor(float(curr)/2))

        dheap[l] += 1
        dheap[r] += 1

        if 0 < dheap[curr]:
            curr = curr
        elif 0 < dheap[curr-1]:
            curr = curr -1

        elif 0 < dheap[math.ceil((curr+1.0)/2)]:
            curr = math.ceil((curr+1.0)/2)
        elif 0 < dheap[math.floor((curr+1.0)/2)]:
            curr = math.floor((curr+1.0)/2)

        elif 0 < dheap[math.ceil((curr+0.0)/2)]:
            curr = math.ceil((curr+0.0)/2)
        elif 0 < dheap[math.floor((curr+0.0)/2)]:
            curr = math.floor((curr+0.0)/2)

        elif 0 < dheap[math.ceil((curr-1.0)/2)]:
            curr = math.ceil((curr-1.0)/2)
        elif 0 < dheap[math.floor((curr-1.0)/2)]:
            curr = math.floor((curr-1.0)/2)
        else:
            for j in xrange(curr, 0, -1):
                if 0 < dheap[j]:
                    curr = j
                    break
            return 0, 0


    left, right = max(l, r), min(l, r)
    return left, right

def compute5(n,m):
    numbers={}
    numbers[n]=1
    current=n
    while m>0:
        l, r = int(math.ceil(float(current-1)/2)), int(math.floor(float(current-1)/2))
        l, r= max(l, 0), max(r,0)
        if current in numbers:
            if numbers[current]<=m:
                m-=numbers[current]
                numbers[l]=numbers.get(l,0)+numbers[current]
                numbers[r]=numbers.get(r,0)+numbers[current]
            else:
                return max(r, l), min(r, l)
        x=sorted(numbers.keys())
        t=x.index(current)
        current=x[t-1]

    return max(r, l), min(r, l)

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
      spots, fills = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      l, r = compute5(spots, fills)
      print "Case #{}: {} {}".format(i, l, r)
