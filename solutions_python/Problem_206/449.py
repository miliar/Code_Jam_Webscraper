def run(case_num):
    dist, num_horses = [int(x) for x in input().strip().split()]
    max_time = -1
    for h in range(num_horses):
        pos, speed = [int(x) for x in input().strip().split()]
        h_dist = dist - pos
        time = h_dist / speed
        max_time = max(time, max_time)
    print("Case #{}: {:.6f}".format(case_num, dist/max_time))

for case in range(int(input())):
    run(case+1)
