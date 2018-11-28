#!/usr/bin/python

T = int(raw_input().strip())

for t in range(T):
    R, k, N = [int(x) for x in raw_input().strip().split()]
    groups = [int(x) for x in raw_input().strip().split()]
    assert len(groups) == N, "have %d groups instead of %d" % (len(groups), N)

    start_ptr = 0
    money_made = 0
    for r in range(R):
        # run #r
        on_coaster = 0
        ptr = start_ptr
        while 1:
            group = groups[ptr]
            if on_coaster + group > k: break # coaster full
            on_coaster += group
            ptr += 1
            if ptr == len(groups): ptr = 0
            if ptr == start_ptr: break # run out of groups
        #print "Run #%d: %d people" % (r+1, on_coaster)
        money_made += on_coaster
        start_ptr = ptr
    print "Case #%d: %d" % (t+1, money_made)
