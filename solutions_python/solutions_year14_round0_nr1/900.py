def get_candidate_set():
    ans_row = int(raw_input()) - 1
    for i in xrange(4):
        line = map(int, raw_input().strip().split(' '))
        if i == ans_row:
            ret = set(line)
    return ret

def solve():
    first = get_candidate_set()
    second = get_candidate_set()
    possible_ans = first.intersection(second)
    if len(possible_ans) == 0: return 'Volunteer cheated!'
    if len(possible_ans) >= 2: return 'Bad magician!'
    return str(possible_ans.pop())

t = int(raw_input())
for i in xrange(1, t+1):
    print "Case #%d:" % i, solve()
