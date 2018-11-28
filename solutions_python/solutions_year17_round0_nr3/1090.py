from heapq import heappush, heappop
from tqdm import tqdm

def bathroom(n, k):
    count = 0
    heap = [-n]

    while count <k:
        selected = -1*heappop(heap)
        if selected>1:
            new_intervals = [selected/2]*2 if selected %2 ==1 else [selected/2, selected/2-1]
            heappush(heap, -1*new_intervals[0])
            heappush(heap, -1*new_intervals[1])
        else:
            new_intervals = [0, 0]
        count+=1
    return max(new_intervals), min(new_intervals)

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())

    for i in tqdm(xrange(1, T + 1)):
      n, k = f.readline().strip().split(" ")
      big, small = bathroom(int(n), int(k))
      print "Case #{}: {} {}".format(i, big, small)




