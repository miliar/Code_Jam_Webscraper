import heapq

def stall_distances(stalls, people):
    empty_runs = [-stalls]
    for i in range(people-1):
        largest = (-heapq.heappop(empty_runs)) - 1
        if largest // 2:
            heapq.heappush(empty_runs, -(largest // 2))
        if (largest + 1) // 2:
            heapq.heappush(empty_runs, -((largest + 1) // 2))
    largest = -heapq.heappop(empty_runs)
    return largest // 2, int((largest - 1) / 2)

# Process input
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        stalls, people = tuple(int(i) for i in input().split())
        max_dist, min_dist = stall_distances(stalls, people)
        print("Case #{}: {} {}".format(i+1, max_dist, min_dist))
