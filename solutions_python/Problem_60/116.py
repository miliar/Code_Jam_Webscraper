#!/usr/bin/python
def solve(n, k, b, t, locations, velocities):
    print n, k, b, t, locations, velocities
    w = []
    for i in xrange(n):
        w.append((t * velocities[i]) + locations[i])
    print w

    x = filter(lambda x: x >= b, w)
    if len(x) < k:
        return -1

    for i in xrange(n - 1, -1, -1):
        if w[i] >= b:
            del w[i]
            k = k - 1    
        else:
            break

    print "--", w, k
    if k <= 0:
        return 0

    swap = 0
    while k > 0:
        n = len(w)
        for i in xrange(n - 1, -1, -1):
            if w[i] < b:
                swap = swap + 1
            else:
                del w[i]
                k = k - 1
                break
        print "--", w, k
    

    return swap
    

def main():
    """docstring for main"""
    input = open("problem")
    ilines = [l.strip() for l in input.readlines()]
    num_tests = int(ilines[0], 0)
    ans = file("answer", "w")
    line_num = 1
    for test in xrange(num_tests):
        line = ilines[line_num]
        (n, k, b, t) = [int(x, 0) for x in line.split()]
        line_num = line_num + 1
        line = ilines[line_num]
        locations = [int(x, 0) for x in line.split()]
        line_num = line_num + 1
        line = ilines[line_num]
        velocities = [int(x, 0) for x in line.split()]
        line_num = line_num + 1
        x = solve(n, k, b, t, locations, velocities)
        if x == -1:
            a = "Case #%d: IMPOSSIBLE\n" % (test + 1) 
        else:
            a = "Case #%d: %d\n" % (test + 1, x) 
        ans.write(a)
        print a
    ans.close()

if __name__ == '__main__':
    main()        
