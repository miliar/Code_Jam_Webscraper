total_cases = int(raw_input())
for case in range(0,total_cases):
    r1 = int(raw_input()) - 1
    a1 = []
    a1.append(raw_input().split(' '))
    a1.append(raw_input().split(' '))
    a1.append(raw_input().split(' '))
    a1.append(raw_input().split(' '))
    r2 = int(raw_input()) - 1
    a2 = []
    a2.append(raw_input().split(' '))
    a2.append(raw_input().split(' '))
    a2.append(raw_input().split(' '))
    a2.append(raw_input().split(' '))
    row1 = a1[r1]
    row2 = a2[r2]
    ret = set(row1).intersection(set(row2))
    if len(ret) == 0:
        answer = "Case #" + str(case+1) + ": Volunteer cheated!"
    elif len(ret) == 1:
        answer = "Case #" + str(case+1) + ": " + list(ret)[0]
    else:
        answer = "Case #" + str(case+1) + ": Bad magician!"
    print answer