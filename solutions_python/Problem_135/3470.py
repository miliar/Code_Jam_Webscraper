from operator import mul
import sys


(WAIT_TOTAL,
 WAIT_1_ANS,
 WAIT_1_ARR,
 WAIT_2_ANS,
 WAIT_2_ARR) = range(5)


def process_input():

    cases_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        if line != '':

            if state == WAIT_TOTAL:
                c = long(line)
                state = WAIT_1_ANS
            elif state == WAIT_1_ANS:
                cases_count += 1
                assert cases_count <= c
                ans_1 = long(line)
                arr_1 = []
                state = WAIT_1_ARR
            elif state == WAIT_1_ARR:
                arr_line = map(long, line.split(' '))
                arr_1.append(arr_line)
                if len(arr_1) == 4:
                    state = WAIT_2_ANS
            elif state == WAIT_2_ANS:
                ans_2 = long(line)
                arr_2 = []
                state = WAIT_2_ARR
            elif state == WAIT_2_ARR:
                arr_line = map(long, line.split(' '))
                arr_2.append(arr_line)
                if len(arr_2) == 4:
                    state = WAIT_1_ANS
                    ret = process_case(ans_1, ans_2, arr_1, arr_2)
                    print 'Case #{}: {}'.format(cases_count, ret)
            else:
                assert False


def process_case(ans_1, ans_2, arr_1, arr_2):
    BAD_MAGICIAN = 'Bad magician!'
    VOLUNTEER_CHEATED = 'Volunteer cheated!'

    candidates_1 = arr_1[ans_1 - 1]
    candidates_2 = arr_2[ans_2 - 1]
    candidates = set(candidates_1) & set(candidates_2)

    if len(candidates) == 0:
        return VOLUNTEER_CHEATED
    elif len(candidates) == 1:
        return candidates.pop()
    else:
        return BAD_MAGICIAN


if __name__ == '__main__':
    process_input()
