
def solve(h, dest):
    h.sort(key = lambda x: x[0])
    total_time = 0

    h1 = h[-1][0]
    s1 = h[-1][1]
    for i in xrange(len(h) - 2, -1, -1):
        #h1, s1 = h[i]
        h2, s2 = h[i]
        if s1 >= s2:
            d = h2
            s = s2

        else:
            d = ((h1 * s2) - (h2 * s1)) * 1.0/(s2 - s1)
            t = (d - h1)/s1
            s = s1
            total_time += t
            h1 = d
            s1 = s2
    if len(h) == 1:
        d = h[0][0]
        s = h[0][1]
    t_ann = (dest - d) * 1.0/s
    total_time += t_ann


    return dest/total_time

def solve2(h, dest):
    h.sort(key=lambda x: x[0])
    h1 = h[-1][0]
    s1 = h[-1][1]
    time_for_front = (dest - h1) * 1.0 / s1
    for i in xrange(len(h) - 2, -1, -1):
        h2, s2 = h[i]
        if s1 >= s2:
            h1 = h2
            s1 = s2
            time_for_front = (dest - h1) * 1.0 / s1
        else:
            time_for_back = (dest - h2) * 1.0 / s2
            if time_for_front >= time_for_back:
                pass
            elif time_for_front < time_for_back:
                h1 = h2
                s1 = s2
                time_for_front = time_for_back

    return dest/time_for_front




if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for case in xrange(1, t + 1):
        d, n = [int(x) for x in raw_input().split(' ')]
        h = []
        for i in xrange(n):
            h_details = [int(x) for x in raw_input().split(' ')]
            h.append(h_details)  # tuple of h_loc, h_speed

            #res = solve(h, d)
        res2 = solve2(h, d)
        #print "Case #{}: {:.6f}".format(case, res)
        print "Case #{}: {:.6f}".format(case, res2)