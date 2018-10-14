import sys, itertools
cases = int(sys.stdin.readline())
case = 0

DEBUG=False

def atleast_min_score(total_score, min_score, surprising=False):
    if not surprising:
        score = total_score // 3
        score3 = score * 3
        if score3 == total_score:
            return score >= min_score
        else:
            return score+1 >= min_score
    else:
        score = total_score // 3
        score3 = score * 3
        if score3 == total_score:
            return 1 <= score <= 9 and score+1 >= min_score
        elif score3 + 1 == total_score:
            return score+1 >= min_score
        else:
            return score+2 >= min_score

while case < cases:

    print("Case #%d:" % (case+1), end=" ")
    case += 1

    line = sys.stdin.readline().split()
    
    surprising, p = [int(x) for x in line[1:3]]
    total_scores = [int(x) for x in line[3:]]
    
    satisfies_min_score = [(atleast_min_score(total_score, p, False), atleast_min_score(total_score, p, True)) for total_score in total_scores]
    
    normal_googlers, surprising_googlers, both_googlers, none_googlers = 0, 0, 0, 0
    for n, s in satisfies_min_score:
        if (n, s) == (False, False):
            none_googlers += 1
        elif (n, s) == (False, True):
            surprising_googlers += 1
        elif (n, s) == (True, False):
            normal_googlers += 1
        elif (n, s) == (True, True):
            both_googlers += 1
            
#    if surprising_googlers >= surprising:
#        googlers = both_googlers + normal_googlers + surprising
#    else:

    googlers = both_googlers + normal_googlers + min(surprising, surprising_googlers)

    if DEBUG:
        print(satisfies_min_score, (normal_googlers, surprising_googlers, both_googlers, none_googlers), end="; ")

    print(googlers)
    


