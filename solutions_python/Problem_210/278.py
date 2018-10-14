EMPTY = 0
C_START = 1
C_END = 2
J_START = 3
J_END = 4

def solve(A_C, A_J, CD, JK):
    CD.sort(key=lambda x: x[0])
    JK.sort(key=lambda x: x[0])
    TimeList = [0] * 24 * 60
    sum_C = 0
    sum_J = 0
    for x in CD:
        TimeList[x[0]] = C_START
        TimeList[x[1] - 1] = C_END
        sum_C += x[1] - x[0]
    for x in JK:
        TimeList[x[0]] = J_START
        TimeList[x[1] - 1] = J_END
        sum_J += x[1] - x[0]
    FreeTime = [[], []]
    prev_state = EMPTY
    prev_time = 0
    for i in range(len(TimeList)):
        state = TimeList[i]
        if state != EMPTY:
            if state == C_START and prev_state == C_END:
                FreeTime[0].append(i - prev_time - 1)
            if state == J_START and prev_state == J_END:
                FreeTime[1].append(i - prev_time - 1)
            prev_state = state
            prev_time = i
    for i in range(len(TimeList)):
        state = TimeList[i]
        if state != EMPTY:
            if state == C_START and prev_state == C_END:
                FreeTime[0].append(i - (prev_time - 1200) - 1)
            if state == J_START and prev_state == J_END:
                FreeTime[1].append(i - (prev_time - 1200) - 1)
            prev_state = state
            prev_time = i
            break
    killed_C = 0
    killed_J = 0
    FreeTime[0].sort()
    FreeTime[1].sort()
    for x in FreeTime[0]:
        if x + sum_C > 720:
            break
        else:
            sum_C += x
            killed_C += 1
    for x in FreeTime[1]:
        if x + sum_J > 720:
            break
        else:
            sum_J += x
            killed_J += 1
    work_C = A_C - killed_C
    work_J = A_J - killed_J
    return max(work_C, work_J) * 2

T = input()
for t in range(1, T+1):
    A_C, A_J = map(int, raw_input().split())
    CD = []
    for i in range(A_C):
        CD.append(map(int, raw_input().split()))
    JK = []
    for i in range(A_J):
        JK.append(map(int, raw_input().split()))
    print 'Case #%d: %d'%(t, solve(A_C, A_J, CD, JK))
