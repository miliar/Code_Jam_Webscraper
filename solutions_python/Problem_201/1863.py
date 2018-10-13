def get_l_r(stalls, idx):
    for i, s in enumerate(stalls[idx+1:]):
        if s:
            right = i
            break
    for i in range(idx-1, -1, -1):
        if stalls[i]:
            left = idx - i - 1
            break
    return left, right


with open('C-small-1-attempt1.in', 'r') as f:
    tasks = [l.strip().split() for l in f.readlines()[1:]]

for task_idx, t in enumerate(tasks):
    stall_num, people = int(t[0]), int(t[1])
    if people in (stall_num, ):
        min_l_r, max_l_r = 0, 0
    else:
        stalls = [1] + [0 for _ in range(stall_num)] + [1]
        empty_stalls = range(1, stall_num+1)
        while True:
            best_min, best_max, best_idx = 0, 0, len(stalls)
            for current_idx in empty_stalls:
                left, right = get_l_r(stalls, current_idx)
                current_min, current_max = min(left, right), max(left, right)
                choose_current = False
                if current_min > best_min:
                    choose_current = True
                elif current_min == best_min:
                    if current_max > best_max:
                        choose_current = True
                    elif current_max == best_max:
                        if current_idx < best_idx:
                            choose_current = True
                if choose_current:
                    best_min, best_max, best_idx = current_min, current_max, current_idx
            stalls[best_idx] = 1
            empty_stalls.remove(best_idx)
            people -= 1
            if not people:
                min_l_r, max_l_r = best_min, best_max
                break
    print 'Case #{}:'.format(task_idx+1), max_l_r, min_l_r
