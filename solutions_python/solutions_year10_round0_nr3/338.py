

def solve_rollers(R,k,gs):
    if k >= sum(gs):
        return sum(gs) * R
    
    start_at = [-1] * len(gs)
    rev = []
    
    ng = 0
    riden = 0
    while riden < R:
        if start_at[ng] != -1:
            break
        start_at[ng] = riden
        rides = 0
        while True:
            if rides + gs[ng] > k:
                break
            rides += gs[ng]
            ng = (ng + 1) % len(gs)
        rev.append(rides)
        riden += 1

    res = sum(rev)
    if riden < R:
        chain_start = start_at[ng]
        chain_length = riden - chain_start
        n_full_chains = int((R - riden) / chain_length)
        chain_rev = sum(rev[chain_start:])
        res += chain_rev * n_full_chains
        
        tail_length = (R - riden) % chain_length
        res += sum(rev[chain_start:chain_start+tail_length])
    return res
    

with open("output.txt", "w") as outf:
    with open("input.txt") as f:
        T = int(f.readline().strip())
        for i in range(T):
            ts = f.readline().strip().split()
            R = int (ts[0])
            k = int (ts[1])
            gs = [int(g) for g in f.readline().strip().split()]
            y = solve_rollers (R, k, gs)
            outf.write("Case #%d: %s\n" % ((i+1),y))