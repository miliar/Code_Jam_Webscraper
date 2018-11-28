import logging
import Queue as Q
import math
import pprint

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def merge_activies(activities, left_time):
    merge_index = -1
    cur_smallest_gap = 999
    for i in xrange(len(activities)-1):
        gap = activities[i+1][0] - activities[i][1]
        if gap < cur_smallest_gap:
            cur_smallest_gap = gap
            merge_index = i

    if cur_smallest_gap > left_time:
        return -1
    new_act = (activities[merge_index][0], activities[merge_index+1][1])
    left_time -= (activities[merge_index+1][0]-activities[merge_index][1])
    del activities[merge_index+1]
    del activities[merge_index]
    activities.insert(merge_index, new_act)
    return left_time

def compute(A_C,A_J,C,J):
    # TODO: insert activities & merge
    C_left_time, J_left_time = 720,720
    for act in A_C:
        C_left_time -= (act[1]-act[0])
    for act in A_J:
        J_left_time -= (act[1]-act[0])

    while True:
        # print A_C, C_left_time
        # print A_J, J_left_time
        merge_C_result = merge_activies(A_C, C_left_time)
        if merge_C_result != -1:
            C_left_time = merge_C_result
        merge_J_result = merge_activies(A_J, J_left_time)
        if merge_J_result != -1:
            J_left_time = merge_J_result
        if merge_C_result == -1 and merge_J_result == -1:
            break

    C_act = A_C[:]
    J_act = A_J[:]
    A_C_i, A_J_i = 0,0
    cur_act = 'Z'
    while A_C_i < len(A_C) or A_J_i < len(A_J):
        if A_J_i >= len(A_J) or (A_C_i < len(A_C) and A_C[A_C_i][0] < A_J[A_J_i][0]):
            if cur_act == 'C':
                J_act.append((A_C[A_C_i][0], A_C[A_C_i][0]))
            cur_act = 'C'
            A_C_i += 1
        elif A_C_i >= len(A_C) or A_C[A_C_i][0] > A_J[A_J_i][0]:
            if cur_act == 'J':
                C_act.append((A_J[A_J_i][0], A_J[A_J_i][0]))
            cur_act = 'J'
            A_J_i += 1
        else:
            assert(False)


    merged_activities = []
    for act in C_act:
        merged_activities.append((act[0], act[1], 'C'))
    for act in J_act:
        merged_activities.append((act[0], act[1], 'J'))
    merged_activities.sort()

    if merged_activities[0][2] == 'C' and merged_activities[-1][2] == 'C':
        if merged_activities[0][0]+1440-merged_activities[-1][1] <= C_left_time:
            del C_act[-1]
        else:
            J_act.append((0,0))
    if merged_activities[0][2] == 'J' and merged_activities[-1][2] == 'J':
        if merged_activities[0][0]+1440-merged_activities[-1][1] <= J_left_time:
            del J_act[-1]
        else:
            C_act.append((0,0))
    # print C_act
    # print J_act

    assert(len(C_act) == len(J_act))
    return 2*len(C_act)

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    # N = int(raw_input())
    C,J= [int(x) for x in raw_input().split(" ")]
    A_C = []
    for _ in xrange(C):
        A_C.append([int(x) for x in raw_input().split(" ")])
    A_C.sort()
    A_J = []
    for _ in xrange(J):
        A_J.append([int(x) for x in raw_input().split(" ")])
    A_J.sort()

    result = compute(A_C,A_J,C,J)
    # correct_compute(grid)
    print "Case #{}: {}".format(i, result)
