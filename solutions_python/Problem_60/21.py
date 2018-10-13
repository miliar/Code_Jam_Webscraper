import re
from fractions import Fraction

# class Rec : pass

def process_case() :
    N, K, B, T = map(int, raw_input().split())
    X = map(int, raw_input().split())
    V = map(int, raw_input().split())

    arrive = []
    possible = []
    poss_count = 0
    for i in range(0, N) :
        a = Fraction(B-X[i]) / V[i]
        arrive.append(a)
        p = (a<=T)
        possible.append( p )
        if p :
            poss_count += 1
    if poss_count < K :
        return "IMPOSSIBLE"

    #recs = []
    #for i in range(0, N) :
    #    recs.append( (X[i], possible[i]) )
    #recs.sort(key=lambda a:a[0])
    #print recs

    fail = 0
    swapped = 0
    succeed = 0
  
    if succeed==K :
        return "%d" % swapped
    for i in range(N-1, -1, -1) :
        if not possible[i] :
            fail += 1
        else :
            swapped += fail
            succeed += 1

            if succeed==K :
                return "%d" % swapped
    print N, K, B, T
    print fail, swapped, succeed
    assert False


if __name__ == "__main__" :
    case_num = int(raw_input())
    for i in range(case_num) :
        result = process_case()
        print "Case #%d: %s" % (i+1, result)
