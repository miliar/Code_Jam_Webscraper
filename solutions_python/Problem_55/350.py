import sys

def one_ride(k, queue):
    n=0
    riders=0
    while queue != [] and riders+queue[0] <= k:
        n += 1
        riders += queue[0]
        queue = queue[1:]
    return n,riders
    

def run_case(casenum):
    R,k,N = map(int,sys.stdin.readline().split())
    g = map(int,sys.stdin.readline().split())
    assert len(g) == N

    queue = g[:]
    cache = [None]*N
    curr_idx=0
    euros_head = 0
    runs_head=0
    for i in xrange(1,R+1):
        #print "idx=%d\tcache=%s\tqueue=%s" % (curr_idx, cache, queue)
        if cache[curr_idx] != None:
            break
        groups_taken,riders = one_ride(k, queue)
        euros_head += riders
        cache[curr_idx] = groups_taken,riders
        queue = queue[groups_taken:] + queue[:groups_taken]
        curr_idx = (curr_idx+groups_taken)%N
        runs_head += 1
    else:
        result = euros_head
        print "Case #%d: %s" % (casenum, euros_head)
        return
    #print "cache=%s\tqueue=%s" % (cache,queue)
    euros_per_loop = 0
    loop_start_idx = curr_idx
    for i in xrange(1,runs_head+1):
        groups_taken,riders = cache[curr_idx]
        euros_per_loop += riders
        curr_idx = (curr_idx+groups_taken)%N
        if curr_idx == loop_start_idx:
            cycle_len = i
            break
    else:
        assert False
    left = R - runs_head
    num_loops = left//cycle_len
    num_tail = left%cycle_len
    euros_tail = 0
    curr_idx = loop_start_idx
    for i in xrange(num_tail):
        groups_taken,riders = cache[curr_idx]
        euros_tail += riders
        curr_idx = (curr_idx+groups_taken)%N
    result = euros_head + num_loops*euros_per_loop + euros_tail
    print "Case #%d: %s" % (casenum,result)

def main():
    T = int(sys.stdin.readline())
    for i in xrange(1,T+1):
        run_case(i)

if __name__ == '__main__':
    main()
