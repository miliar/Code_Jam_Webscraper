def insertperson(stall, last=False):
    curr = 0
    start = 0
    curr_streak = 0
    streak = 0
    index = 0
    for x in stall:
        if x == 1:
            if curr_streak > streak:
                streak = curr_streak
                start = curr
            curr_streak = 0
            curr = index
        else:
            curr_streak += 1
        index += 1
    if len(stall) % 2:
        new_pos = start + (streak + 1) // 2
    else:
        new_pos = start + (streak + 1) // 2

    if last:
        left = 0
        right = 0
        while (stall[new_pos - left - 1] != 1):
            left += 1
        while (stall[new_pos + right + 1]) != 1:
            right += 1
        return [max(left, right), min(left, right)]
    stall[new_pos] = 1
    return stall

def handler(k, people):
    if k == people or k == (people - 1):
        return [0, 0]
    stalls = [0] * (k + 2)
    stalls[0] = 1
    stalls[-1] = 1

    for i in range(people - 1):
        stalls = insertperson(stalls)
    return insertperson(stalls, True)



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    result = handler(n, m)
    print("Case #{}: {} {}".format(i, result[0], result[1]))