def optimize(x, walk, run, t, walkways):
    walkways.sort(key=lambda (beginning, end, speed):beginning)
    a = 0
    zeroes = []
    for (beginning, end, speed) in walkways:
        zeroes.append((a, beginning, 0))
        a = end
    zeroes.append((a, x, 0))
    
    walkways = sorted(walkways + zeroes, key=lambda (beginning, end, speed):speed)
    
    total = 0
    for (beginning, end, speed) in walkways:
        if (end - beginning) == 0:
            continue
        runtime = 1.0 * (end - beginning) / (speed + run)
        if t >= runtime:
            t -= runtime
            total += runtime
        else:
            total += t
            runlength = (speed + run) * t
            walklength = (end - beginning - runlength)
            total += 1.0 * walklength / (speed + walk)
            t = 0
    return total



#print optimize(10, 1, 4, 1, [(4, 6, 1), (6, 9, 2)])


def main():
    cases = int(raw_input())
    for case in range(cases):
        (x, walk, run, t, N) = map(int, raw_input().split(" "))
        walkways = []
        for i in range(N):
            walkways.append(tuple(map(int, raw_input().split(" "))))

        total = optimize(x, walk, run, t, walkways)
        print "Case #%d: %s" % (case+1, total)

main()

