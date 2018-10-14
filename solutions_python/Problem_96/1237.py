# n   n mod 3     n/3     range   xrange
# 18      0       6       6       5,6,7
# 19      1       6       6,7     5,7
# 20      2       6       6,7     6,7,8

def read_input():
    f = open('B-large.in')
    num_cases = int(f.readline())
    cases = list()
    for i in range(num_cases):
        cases.append([int(x) for x in f.readline().split(' ')])
    f.close()
    return cases

def get_range(score, is_surprising):
    if score == 0:
        if is_surprising:
            return []
        return [0]
    if score == 1:
        if is_surprising:
            return []
        return [0,1]
    if score == 2:
        if is_surprising:
            return [0,2]
        return [0,1]
    normal_score_table = [[0], [0,1], [0,1]]
    surprising_score_table = [[-1,0,1], [-1,1], [0,1,2]]
    if is_surprising:
        score_table = surprising_score_table
    else:
        score_table = normal_score_table
    return [x + score/3 for x in score_table[score%3]]

cases = read_input()
case_index = 1
for scores in cases:
    N = scores.pop(0) # number of googlers
    S = scores.pop(0) # number of surprising triplets
    p = scores.pop(0) # score threshold
    assert N == len(scores)
    scores.sort()
    answer = 0
    #print scores,'needs at least',p,'with',S,'surprising triplets'
    for score in scores:
        if max(get_range(score, False)) >= p:
            answer += 1
        elif S > 0 and score >= 2 and max(get_range(score, True)) >= p:
            answer += 1
            S -= 1
    print 'Case #%d: %d' % (case_index, answer)
    case_index += 1

