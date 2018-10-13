import heapq

def result(n, k):
    n, k = int(n), int(k)
    q = [-n]
    for i in range(k-1):
        top = heapq.heappop(q)
        if top % 2:
            heapq.heappush(q, (top + 1) // 2)
            heapq.heappush(q, (top + 1) // 2)
        else:
            heapq.heappush(q, top/2)
            heapq.heappush(q, (top/2)+1)
    top = -1*heapq.heappop(q)
    print('done', n,k,top)
    if top % 2:
        return '%d %d' % (top/2, top/2)
    else:
        return '%d %d' % (top/2, (top/2) - 1)

if __name__ == "__main__":
    FILE_NAME = 'C-small-2-attempt0'
    with open(FILE_NAME + '.in') as f:
        with open(FILE_NAME + '.out', 'w') as w:
            r = f.readlines()

            for i in range(len(r) - 1):
                w.write('Case #%d: %s\n' % (i + 1, result(*r[i + 1].split())))