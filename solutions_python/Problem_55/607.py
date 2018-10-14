import sys

lines = sys.stdin.readlines()
cases = int(lines[0])

for i in xrange(cases):
    earnings = 0

    in1 = lines[2*i + 1]
    in2 = lines[2*i + 2]

    params = in1.strip().split(' ')

    R,k,N = int(params[0]), int(params[1]), int(params[2])
    groups = map(int, in2.strip().split(' '))

    grp_ptr = 0
    for _ in xrange(R):
        current_load = 0
        start_ptr = grp_ptr

        while current_load < k:
            if start_ptr == grp_ptr and current_load != 0:
                break

            if current_load + groups[grp_ptr] <= k:
                current_load += groups[grp_ptr]
                grp_ptr += 1

                if grp_ptr == len(groups):
                    grp_ptr = 0
            else:
                break

        earnings += current_load

    print 'Case #%d: %d' % (i+1, earnings)
