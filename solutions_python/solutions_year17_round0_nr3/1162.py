import heapq

T = int(input())

def solve(n,k):
    h = [-n]

    for i in range(k):
        c = heapq.heappop(h)
        last = -c 
        if -c == 2:
            heapq.heappush(h,-1)
        elif -c == 1:
            pass
        else:
            current = -c - 1
            heapq.heappush(h, -(current // 2))
            if current % 2:
                heapq.heappush(h, -(current // 2 + 1))
            else:
                heapq.heappush(h, -(current // 2))
    return(last)
        

for i in range(1, T+1):
    n,k = map(int, input().split())
    ans = solve(n,k) 
    print("Case #{}: {} {}".format(i, ans // 2, ans // 2 if ans % 2 else ans // 2 - 1))