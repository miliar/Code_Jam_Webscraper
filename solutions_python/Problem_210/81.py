import sys

stdout = sys.stdout
stdin = sys.stdin
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def solve():
    result = 0
    Ac, Aj = map(int, input().split())
    c_activities = []
    for i in range(Ac):
        c_activities.append(list(map(int, input().split())))
        #c_activities[i].append(1)
    j_activities = []
    for i in range(Aj):
        j_activities.append(list(map(int, input().split())))
        #j_activities[i].append(1)

    #if max(Ac,Aj) <= 1:
    #    return 2
            
    c_activities.sort(key=lambda x: x[0])
    j_activities.sort(key=lambda x: x[0])

    #print(c_activities)
    #print(j_activities)

    
    c = 0
    j = 0
    c_combines = []
    while c < len(c_activities)-1:
        between = False
        while j < len(j_activities):
            if j_activities[j][0] >= c_activities[c][1]:
                if j_activities[j][1] <= c_activities[c+1][0]:
                    between = True
                break
            j += 1
        if not between:
            c_combines.append(c_activities[c+1][0] - c_activities[c][1])
            #c_activities[c] = [c_activities[c][0], c_activities[c+1][1], c_activities[c][2] + c_activities[c+1][2]]
            #c_activities.pop(c+1)
        c += 1


    c = 0
    j = 0
    j_combines = []
    while j < len(j_activities)-1:
        between = False
        while c < len(c_activities):
            if c_activities[c][0] >= j_activities[j][1]:
                if c_activities[c][1] <= j_activities[j+1][0]:
                    between = True
                break
            c += 1
        if not between:
            j_combines.append(j_activities[j+1][0] - j_activities[j][1])
            #j_activities[j] = [j_activities[j][0], j_activities[j+1][1], j_activities[j][2] + j_activities[j+1][2]]
            #j_activities.pop(j+1)
        j += 1

    if len(j_activities) == 0 and len(c_activities) == 0:
        pass
    elif len(j_activities) == 0:
        c_combines.append(c_activities[0][0] - c_activities[len(c_activities)-1][1] + 1440)
    elif len(c_activities) == 0:
        j_combines.append(j_activities[0][0] - j_activities[len(j_activities)-1][1] + 1440)
    elif c_activities[len(c_activities)-1][1] > j_activities[len(j_activities)-1][1]:
        if c_activities[0][0] < j_activities[0][0]:
            c_combines.append(c_activities[0][0] - c_activities[len(c_activities)-1][1] + 1440)
    else:
        if j_activities[0][0] < c_activities[0][0]:
            j_combines.append(j_activities[0][0] - j_activities[len(j_activities)-1][1] + 1440)

    c_combines.sort()
    j_combines.sort()

    c_remaining = 720
    j_remaining = 720
    for a in c_activities:
        c_remaining -= a[1] - a[0]
    for a in j_activities:
        j_remaining -= a[1] - a[0]

    C = len(c_activities)
    J = len(j_activities)

    for dur in c_combines:
        if dur <= c_remaining:
            c_remaining -= dur
            C -= 1
        else:
            break

    for dur in j_combines:
        if dur <= j_remaining:
            j_remaining -= dur
            J -= 1
        else:
            break

    #print(c_activities)
    #print(j_activities)
    #print(c_combines)
    #print(j_combines)

    return max(C, J, 1) * 2

T = int(input())
for CASE in range(1,T+1):
    print('Case #' + str(CASE) + ': ', end='')
    print(solve())

sys.stdout = stdout
sys.stdin = stdin
