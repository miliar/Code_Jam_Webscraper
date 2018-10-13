import sys

def dancing_googlers(scores,target_score,special_cases):
    discarded = 0
    need_special = 0
    ok = 0

    for score in scores:
        rest = -1 * (score-3*target_score)
        if score < target_score:
            discarded += 1
        elif rest <= 2:
            ok += 1
        elif 3 <= rest <= 4:
            need_special += 1
        else:
            discarded += 1
    return ok + min(special_cases,need_special)
#    cases = no_special + canbe_special
#    if special_cases <= need_special: 
#        return cases + special_cases
#    elif (special_cases - need_special) <= (discarded + canbe_special):
#        return cases + need_special
#    else:
#        max_no_special = len(scores) - special_cases
#        return need_special + canbe_special + max_no_special



out_f = open(sys.argv[2],'w')
with open(sys.argv[1]) as in_f:
    T = int(in_f.readline())
    for t in range(T):
        N,S,p,scores = in_f.readline().split(None,3)
        scores = [int(a) for a in scores.split()]
        print >> out_f, "Case #%d: %d" % (t+1,dancing_googlers(scores,int(p),int(S)))





