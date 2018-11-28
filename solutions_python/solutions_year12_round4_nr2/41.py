import sys

def solve(w,h,radii):
    w,h,radii

    # do a line search
    radii = [(r,i) for (i,r) in enumerate(radii)]
    radii.sort()
    radii.reverse()
    # x,y  0 <= x <= W

    active = []
    # active is left, right, top

    next_row = 0

    # special case for the first row.
    results = [0] * len(radii)
    
    while radii:
        # print
        # print "radii", radii
        # print "active", active
        

        row = next_row
        # print "row", row
        active = [(x,y,t) for (x,y,t) in active if t > row]

        if not active:
            r, idx = radii[0]
            active.append((0, r, 2*r + row))

            results[idx] = (0, r + row)
            radii = radii[1:]
            continue

        next_row = row

        blocked = sorted(active)
        # print "blocked", blocked
        added = False
        for i in xrange(len(blocked)+1):
            if i == 0:
                max_r,left = blocked[i][0], -1e99
            elif i == len(blocked):
                max_r,left = w - blocked[i-1][1], 1e99
            else:
                max_r,left = (blocked[i][0] - blocked[i-1][1]) * 0.5, blocked[i-1][1]
            
            # print "max_r, left", max_r, left
            for rad_idx in xrange(len(radii)):
                r = radii[rad_idx][0]
                if r <= max_r:
                    if left == -1e99:
                        c = 0
                    elif left == 1e99:
                        c = w
                    else:
                        c = left + r
                    # print "adding results", c, row + r
                    results[radii[rad_idx][1]] = c, row + r
                    # print results
                    active.append((c-r, c+r, row+2*r))
                    radii = radii[:rad_idx] + radii[rad_idx+1:]
                    added = True
                    break
        if not added:
            # print "didn't add anything"
            next_row = min(t for (x,y,t) in active)
            
    # print "results:", results
    return " ".join("%d %d" % x for x in results)
        
    
        


def main(lines):
    T = int(lines.next())
    for case in xrange(1,T+1):
        N, w,h  = map(int, (lines.next().split()))
        radii = map(int, lines.next().split())
        r = solve(w,h,radii)
        print "Case #%d: %s" % (case, r)


"""


"""

if __name__ == "__main__":
    if sys.argv < 2:
        print "need a file name!"
    main(open(sys.argv[1]))
    # main(sys.stdin)
    



