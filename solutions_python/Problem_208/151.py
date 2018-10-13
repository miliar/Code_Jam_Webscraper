T = int(input())

def update_herd(herd, dist_to_nxt, new_horse):
    surviving_herd = [(v, s-dist_to_nxt, t + dist_to_nxt / v) for
                      (v, s, t) in herd if
                      s >= dist_to_nxt]
    best_new_time = min(h[-1] for h in surviving_herd)
    new_v, new_s = new_horse
    surviving_herd.append((new_v, new_s, best_new_time))
    return surviving_herd
    

for test_case_no in range(1, T+1):
    num_cities, num_queries = [int(x) for x in input().split()]

    horses = []
    for _ in range(num_cities):
        s, v= [int(x) for x in input().split()]
        horses.append((v, s))

    dist = []
    for i in range(num_cities):
        row = [int(x) for x in input().split()]
        dist.append(row)

    assert(num_queries == 1)
    input() # read query line    

    dist_arr = [dist[i][i+1] for i in range(num_cities-1)]

    v0, s0 = horses[0]
    horse_vector = [(v0, s0, 0)]

    for i in range(0, num_cities-1):
        #print(horse_vector)
        horse_vector = update_herd(horse_vector, dist_arr[i], horses[i+1])
    #print(horse_vector)
    best_time = min(h[-1] for h in horse_vector)
    print("Case #{}: {}".format(test_case_no, best_time))
