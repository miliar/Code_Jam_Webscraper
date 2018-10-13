def dist_free_left(pos, stalls_state):
    return next( l for l in range(pos) if not stalls_state[pos-l-1])

def dist_free_right(pos, stalls_state):
    return next( l for l in range(len(stalls_state) - pos-1) if not stalls_state[pos+l+1] )

def compute_ls_rs(pos, stalls_state):
    """ Assumption: borders are always False"""
    return    dist_free_left(pos,stalls_state) \
            , dist_free_right(pos,stalls_state)


def find_best_stall(stalls_state):
    best_so_far = []
    best_side, other_side = -1,-1
    for pos in ( i for i in range(len(stalls_state)) if stalls_state[i] ):
        cur_ls, cur_rs = compute_ls_rs(pos, stalls_state)
        cur_best_side, cur_other_side = max(cur_ls,cur_rs), min(cur_ls,cur_rs)
        if (cur_other_side,cur_best_side) > (other_side,best_side):
            # invalidate all results, this one is now the (single) best
            best_so_far = [pos, ]
            best_side, other_side = cur_best_side, cur_other_side
        elif (cur_other_side,cur_best_side) == (other_side,best_side):
            # not really useful, as we chose the leftmost in case of tie, keep for debugging
            best_so_far.append(pos)
        else:
            # worse solution, discard it
            pass
    assert best_so_far != []
    return best_so_far[0]

def naive(n,k):
    #bitset "isFree"
    stalls_state = [True,] * (n+2)
    stalls_state[0] = stalls_state[n+1] = False
    # Ls,Rs when all "public" stalls are empty
    # prms = [(i,n-i-1) for i in range(n)]
    pos = None
    for i in range(k):
        pos = find_best_stall(stalls_state)
        stalls_state[pos] = False
    ls, rs =compute_ls_rs(pos, stalls_state)
    return max(ls,rs) , min(ls,rs)

def less_naive(n,k):
    free = [n,]
    new_right, new_left = 0,0
    for i in range(k):
        # pick largest free range, decrease by one, split in two halves
        space = free[0] - 1
        new_left, new_right = space/2, ( (space/2 + 1) if (space % 2) else space/2)
        free = sorted( free[1:] + [new_left,new_right])[::-1]
    return new_right, new_left

def fast(n,k):
    free = {n:1}
    new_right, new_left = 0,0
    for i in range(k):
        # pick largest free range, decrease by one, split in two halves
        largest = max(free.keys())
        cnt = free[largest]
        if free[largest] == 1:
            free.pop(largest)
        else:
            free[largest] = cnt -1
        largest = largest - 1
        new_left, new_right = largest/2, ( (largest/2 + 1) if (largest % 2) else largest/2)
        if new_right > 0:
            if new_left == new_right:
                free[new_left] = free.get(new_left,0) + 2
            else:
                free[new_left] = free.get(new_left,0) + 1
                free[new_right] = free.get(new_right,0) + 1
    return new_right, new_left

def super_fast(n,k):
    """ same idea as in *fast*, but process all chunks of same size at once """
    free = {n:1}
    new_right, new_left = 0,0

    while(k>0):
        # k can become negative, it doesn't affect the relevance of the result
        # pick largest free range, decrease by one, split in two halves
        largest = max(free.keys())
        cnt = free.pop(largest)
        free_range = largest - 1
        new_left = new_right = free_range/2
        if (free_range % 2):
            new_right += 1
            free[new_left] = free.get(new_left,0) + cnt
            free[new_right] = free.get(new_right,0) + cnt
        else: # new_left == new_right:
            free[new_left] = free.get(new_left,0) + (2 * cnt)
        # all the cnt next persons would have the same free range around them
        k -= cnt
    return new_right, new_left

def main(fnStrategy):
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      n, k = [int(s) for s in raw_input().split(" ")]
      min_free,max_free =  fnStrategy(n,k)
      print "Case #{}: {} {}".format(i,min_free,max_free )

main(super_fast)

