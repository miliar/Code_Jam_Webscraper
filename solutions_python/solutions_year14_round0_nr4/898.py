import sys
import os
import bisect 

case_win = "Case #%s: "

def make_work(input='input.txt', output='output.txt'):
    file_in = open(input)
    cases_number = int(file_in.readline().strip())
    for n in xrange(1, cases_number + 1):
        answer = get_answer(file_in)
        print((case_win % n) + str(answer))


def solve_optimal(naomi, ken):
    naomi_score = 0
    ken_score = 0
    while len(naomi) > 0:
        nb = naomi.pop(0)
        if nb > ken[0]:
            naomi_score += 1
            ken.pop(0)
        else:
            ken_score += 1
            ken.pop(-1)
    return naomi_score

def solve_honest(naomi, ken):
    naomi_score = 0
    ken_score = 0
    while len(naomi) > 0:
        nb = naomi.pop(0)
        ken_idx = bisect.bisect_right(ken, nb)
        if ken_idx < len(ken):
            ken.pop(ken_idx)
            ken_score += 1
        else:
            ken.pop(0)
            naomi_score += 1

    return naomi_score

def get_answer(file_in):
    optimal = 0
    honest = 0
    block_count = map(int, file_in.readline().strip())
    
    naomi = sorted(map(float, file_in.readline().strip().split()))
    ken = sorted(map(float, file_in.readline().strip().split()))
    
    optimal = solve_optimal(list(naomi), list(ken))    
    honest = solve_honest(list(naomi), list(ken))    
    return "%s %s" % (optimal, honest)

if len(sys.argv) >= 2:
    make_work(input=sys.argv[1])
else:
    make_work()