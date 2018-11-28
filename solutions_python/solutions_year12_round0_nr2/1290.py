T = input('')

def get_best_nonsurp(total):
    if total == 0: return 0
    if total % 3 == 0:
        return total // 3
    return total // 3 + 1
    
def get_best_surp(total):
    if total == 0: return 0
    if total % 3 == 2:
        return total // 3 + 2
    return total // 3 + 1

for casenr in xrange(T):
    a = map(int, raw_input('').split())
    N,S,p = a[0:3]
    scores = a[3:]
    better_nonsurp = 0
    better_onlysurp = 0
    for x in scores:
        if get_best_nonsurp(x) >= p:
            better_nonsurp += 1
        elif get_best_surp(x) >= p:
            better_onlysurp += 1
    result = better_nonsurp + min(better_onlysurp, S)
    print "Case #%d: %d" % (casenr+1, result)
        
