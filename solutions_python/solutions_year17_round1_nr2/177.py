def is_in_limits(serving_count, required, pack_size):
    if pack_size < 0.9*serving_count*required:
        return -1
    if pack_size > 1.1*serving_count*required:
        return 1
    return 0

def get_max_kits(N, P, required, packages):
    cur_serve = 1
    kit_count = 0
    while True:
        incr_serving = False
        for i in range(0, N):
            while len(packages[i]) > 0 and is_in_limits(cur_serve, required[i], packages[i][0]) == -1:
                packages[i].pop(0)

            if len(packages[i]) == 0:
                return kit_count

            if is_in_limits(cur_serve, required[i], packages[i][0]) == 1:
                incr_serving = True
        if not incr_serving:
            kit_count += 1
            for j in range(0, N):
                packages[j].pop(0)
        else:
            cur_serve += 1

if __name__ == "__main__":
    t = int(raw_input().strip())
    for i in range(0, t):
        N, P = [int(x) for x in raw_input().strip().split(' ')]
        required = [int(x) for x in raw_input().strip().split(' ')]
        packages = []
        for _ in range(0, N):
            pack = [int(x) for x in raw_input().strip().split(' ')]
            pack.sort()
            packages.append(pack)
        ans = get_max_kits(N, P, required, packages)
        print "Case #%d: %d" % ( i + 1, ans )
