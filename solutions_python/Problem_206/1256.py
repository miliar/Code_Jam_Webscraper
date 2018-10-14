

def time_to_reach_d(d, k, s):
    return max(d-k, 0)/s

t = int(input())
for i in range(1, t + 1):
    d, n = (int(s) for s in input().split(" "))
    times_to_reach_destination = []
    for j in range(0, n):
        k, s = (int(s) for s in input().split(" "))
        times_to_reach_destination.append(time_to_reach_d(d, k, s))

    time_for_slowest_horse_to_reach_d = max(times_to_reach_destination)
    print("Case #{}: {:.6f}".format(i, d/time_for_slowest_horse_to_reach_d, 6))