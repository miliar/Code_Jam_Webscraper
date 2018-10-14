def init_stalls(stalls):
    stall_array = [True]
    for idx in range(stalls):
        stall_array.append(False)
    stall_array.append(True)
    return stall_array

def calc_l(stalls, index):
    openings = 0
    current_idx = index - 1
    while True:
        if not stalls[current_idx]:
            openings += 1
            current_idx -= 1
        else:
            break
    return openings

def calc_r(stalls, index):
    openings = 0
    current_idx = index + 1
    while True:
        if not stalls[current_idx]:
            openings += 1
            current_idx += 1
        else:
            break
    return openings

def get_score(stalls, idx):
    left = calc_l(stalls, idx)
    right = calc_r(stalls, idx)
    score = 0
    score += min(left, right) * 1000000
    score += max(left, right) * 1000
    score += len(stalls) - idx
    return score

def get_winning_index(scores):
    return scores.index(max(scores))

def sit_in_stall(stalls):
    # stall score is
    scores = []
    spot = 0
    for current_idx in range(len(stalls)):
        if not stalls[current_idx]:
            scores.append(get_score(stalls, current_idx))
        else:
            scores.append(0)
    print('{}'.format('.'))
    return get_winning_index(scores)

inputname = input('Inputfile: ')
f = open(inputname)
o = open(inputname + '.out', 'w')
count = int(f.readline())
print('processing ' + str(count) + ' entries')
for entry in range(count):
    current = f.readline().strip()
    (stalls, people) = current.split(' ')
    stall_array = init_stalls(int(stalls))
    final_max = 0
    final_min = 0
    if stalls == people:
        o.write('Case #{}: {} {}\n'.format(entry+1, 0, 0))
    else:
        for person in range(int(people)):
            spot_to_sit = sit_in_stall(stall_array)
            final_r = calc_r(stall_array, spot_to_sit)
            final_l = calc_l(stall_array, spot_to_sit)
            final_max = max(final_r, final_l)
            final_min = min(final_r, final_l)
            stall_array[spot_to_sit] = True
        o.write('Case #{}: {} {}\n'.format(entry+1, final_max, final_min))
