T = int(raw_input().strip())

def solve( d, horses ):
    if len(horses) == 0:
        return d

    max_time = float('-inf')
    for dis, speed in horses:
        left = (d-dis)/float(speed)
        max_time = max(max_time, left)

    return d/max_time

for idx in range(1, T+1):
    D, N = map(int, raw_input().split())
    horses = []
    for i in range(N):
        pos, speed = map(int, raw_input().split())
        horses.append([pos, speed])


    """
    if sum(pancakes) == len(pancakes):
        print "Case #%d: %d" % (idx, count)
    else:
        print "Case #%d: IMPOSSIBLE" % (idx)
    """
    print "Case #%d: %f" % (idx, solve(D, horses))
