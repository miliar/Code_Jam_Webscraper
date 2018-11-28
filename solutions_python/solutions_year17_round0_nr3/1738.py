import heapq
def solve():
    dicks = map(lambda x: int(x), raw_input().split())
    h = []
    heapq.heappush(h, -1 * dicks[0])
    for i in range(dicks[1] - 1):
      num = heapq.heappop(h) * -1
      first = (num-1)/2
      second = num - 1- first
      heapq.heappush(h, -1 * first)
      heapq.heappush(h, -1 * second)
    num = heapq.heappop(h) * -1
    first = (num-1) / 2
    second = num - first - 1
    return str(max(first, second)) + " " + str(min(first, second))

num_tests = int(raw_input())

for K in range(num_tests):
    print "Case #" + str(K + 1) + ": " + str(solve())
