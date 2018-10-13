def main():
    T = int(raw_input())
    for t in xrange(T):
        (C, F, X) = (float(x) for x in raw_input().split())
        print "Case #" + str(t+1) + ": " + str(find_optimal(C, F, X))

def find_optimal(farm_cost, farm_revenue, win_count):
    i = 0
    farm_time = get_farm_time(0, i, farm_cost, farm_revenue)
    i += 1
    t0 = win_count/2
    t1 = get_time(farm_time, i, farm_revenue, win_count)
    while t1 < t0:
        t0 = t1
        farm_time = get_farm_time(farm_time, i, farm_cost, farm_revenue)
        i += 1
        t1 = get_time(farm_time, i, farm_revenue, win_count)
    return t0

def get_farm_time(old_farm_time, old_farm_count, farm_cost, farm_revenue):
    return old_farm_time + farm_cost/(2 + old_farm_count * farm_revenue)

def get_time(farm_time, farm_count, farm_revenue, win_count):
    return farm_time + win_count/(2 + farm_count * farm_revenue)

if __name__ == "__main__":
    main()
