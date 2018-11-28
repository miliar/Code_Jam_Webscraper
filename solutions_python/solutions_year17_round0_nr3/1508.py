"""
Bathroom stalls
"""
import heapq

OUTPUT = 'Case #%d: %ld %ld'

def main():
    """
    I/O
    """
    T = int(raw_input().strip())

    for t in range(1, T+1):
        N, K = raw_input().strip().split()
        N = int(N)
        K = int(K)

        #convert to negatives and use as maxheap
        spaces = [-N]
        heapq.heapify(spaces)
        for i in range(1, K):
            width = (0 - heapq.heappop(spaces)) - 1
            left = width / 2
            right = width - left
            heapq.heappush(spaces, 0 - left)
            heapq.heappush(spaces, 0 - right)

        #last person calculation
        lw = (0 - heapq.heappop(spaces)) - 1
        ls = lw / 2
        rs = lw - ls

        #always ls <= rs
        print OUTPUT % (t, rs, ls)

if __name__ == '__main__':
    main()
