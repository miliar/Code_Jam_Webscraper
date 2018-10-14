def is_sol(seq):
    up = True
    for i in range(len(seq)-1):
        if up:
            if seq[i] < seq[i+1]:
                continue
            up = False
        else:
            if seq[i] > seq[i+1]:
                continue
            return False
    return True
            
def num_swaps(seq):
    count = 0
    while len(seq) > 0:
        m = min(seq)
        i = seq.index(m)
        s_left = i
        s_right = len(seq)-i-1
        count += min(s_left, s_right)
        seq.pop(i)
    return count
        
    
T = int(raw_input())
for i in range(1,T+1):
    N = int(raw_input())
    seq = map(int, raw_input().split())
    print "Case #%d: %d" % (i, num_swaps(seq))
    
