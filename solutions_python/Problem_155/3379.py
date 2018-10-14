
with open('A.in', 'r') as f:
    num_cases = int(f.readline())
    for case in range(num_cases):
        line = f.readline()
        Smax = int(line.split()[0])
        audience = [int(x) for x in line.split()[1]]
        cumsum = 0
        num_added = 0
        for i, x in enumerate([int(x) for x in audience]):
            diff = i - cumsum
            if diff > 0:
                num_added += diff
                cumsum += diff
            cumsum += x
        print "Case #%d: %d" % (case + 1, num_added)

