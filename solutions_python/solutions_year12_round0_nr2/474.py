debug = False

def compute_scores(total):
    base_score = total / 3
    remainder = total % 3

    scores = [base_score, base_score, base_score]
    i=0
    while remainder:
        scores[i] += 1
        remainder -=1
        i+=1

    return scores

def filter_good_enough(totals, target_score):
    possible_scores = set(filter(lambda x: x>=target_score, range(11)))
    new_totals = []
    ret = 0
    for total in totals:
        if set(total).intersection(possible_scores):
            ret += 1
        else:
            new_totals.append(total)

    return ret, new_totals

def max_googlers(s):
    if debug:
        print "Data:",s
    data = [int(x) for x in s.split(' ')]
    N = data[0]
    S = data[1]
    p = data[2]
    totals = data[3:3+N]
    if debug:
        print "Googlers:", N
        print "Surprised:", S
        print "Score:", p
        print "Totals:",totals
    min_acceptable_score = p*3-4
    if p == 0: min_acceptable_score = max(0,min_acceptable_score)
    else: min_acceptable_score = max(1,min_acceptable_score)
    totals = filter(lambda x: x>=min_acceptable_score, totals)
    if debug: print "Totals:",totals
    totals = map(compute_scores, totals)
    if debug: print "Totals:",totals
    
    n, totals = filter_good_enough(totals, p)

    return n + min(S,len(totals))


with open("google_dancers.txt") as f:
    rows = int(f.readline().strip())
    for row in range(rows):
        s = f.readline().strip()
        print "Case #%d: %d" % (row+1, max_googlers(s))

