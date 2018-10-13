# https://code.google.com/codejam/contest/1460488/dashboard#s=p1
from sys import stdin as i
import itertools

def max_diff(seq):
    diff_max = 0
    for i,j in itertools.combinations(range(len(seq)), 2):
        diff = abs(seq[i] - seq[j])
        if diff > diff_max: diff_max = diff

    return diff_max

def valid_triplet(t, p):
    if max_diff(t) > 2: return False

    for k in t:
        if k >= p: return True
    
    return False

def final_count(googlers, S):
    count = 0
    for triplets in googlers:
        if len(triplets) < 2:
            if max_diff(triplets[0]) < 2:
                count += 1
            else:
                if S > 0:
                    count += 1
                    S -= 1
        else:
            if any(map(lambda x: max_diff(x) < 2 ,triplets)):
                count += 1
            else:
                count +=1
                S -= 1

    return count

for j in range(int(i.readline())):
    data = i.readline().strip().split()
    N = data[0]
    S = data[1]
    p = data[2]
    t = data[3:]

    res = []
    for ti in t:
        triplets = filter(lambda x: sum(x) == int(ti) and valid_triplet(x, int(p)),
                          itertools.combinations_with_replacement(range(11), 3))
        if triplets: res.append(triplets)
        
    print "Case #%d: %s" % ((j+1), final_count(res, int(S)))
    #print "%s --> t=%s p=%s S=%s" % (res, t, p, S) # Debugging info
