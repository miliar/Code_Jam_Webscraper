import heapq, collections

def main():
    with open('/Users/tengg/Downloads/C-large.in') as f:
        t = int(f.readline())
        for i in range(1, t+1):
            n, k = map(int, f.readline().split(' '))
            print(f"Case #{i}: " + last_stall_bisect(n, k))

def last_stall(n, k):
    heap = [(-n-1, 0, n+1)]
    for _ in range(k-1):
        stall_len, stall_lo, stall_hi = heapq.heappop(heap)
        spot = stall_lo + stall_hi >> 1
        if spot > stall_lo + 1:
            heapq.heappush(heap, (-(spot - stall_lo), stall_lo, spot))
        if stall_hi > spot + 1:
            heapq.heappush(heap, (-(stall_hi - spot), spot, stall_hi))
    _, lo, hi = heapq.heappop(heap)
    spot = lo + hi >> 1
    #print(lo, hi, spot)
    ls = spot - lo - 1
    rs = hi - spot - 1
    return f"{max(ls, rs)} {min(ls, rs)}"

def last_stall_bisect(n, k):
    lo, hi = 0, n+1
    while k > 1:
        mid = lo + hi >> 1
        k -= 1
        if k % 2 == 0:
            hi = mid
            k //= 2
        else:
            lo = mid
            k = k//2 + 1
    mid = lo + hi >> 1
    ls, rs = mid - lo - 1, hi - mid - 1
    return f"{max(ls, rs)} {min(ls, rs)}"

if __name__ == '__main__':
    main()
