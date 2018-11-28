"""
    Oh yeah
    -oooo- -1 4
    -oxoo-  1
    -oxxo-
    -xxxo-

    -ooooo- -1 5
"""

def get_candidate_position(segment):
    a = segment[0]
    b = segment[1]
    if (b-a) % 2 == 1:
        return a + (b-a) / 2
    return a + (b-a) / 2

def get_min(segment, candidate_pos):
    a = segment[0]
    b = segment[1]
    return min(candidate_pos - a, b - candidate_pos)

def get_max(segment, candidate_pos):
    a = segment[0]
    b = segment[1]
    return max(candidate_pos - a, b - candidate_pos)

def person_enters_toilet(toilet_array):
    # Get candidate segments
    candidates = toilet_array[max(toilet_array.keys())]
    mins = map(lambda x : get_min(x, get_candidate_position(x)), candidates)
    best_min = max(mins)
    candidates = [candidates[i] for i, x in enumerate(mins) if x == best_min]
    maxs = map(lambda x : get_max(x, get_candidate_position(x)), candidates)
    best_max = max(maxs)
    candidates = [candidates[i] for i, x in enumerate(maxs) if x == best_max]
    segment = min(candidates, key=lambda x: x[0])
    toilet_array[max(toilet_array.keys())].remove(segment)
    if len(toilet_array[max(toilet_array.keys())]) == 0:
        del toilet_array[max(toilet_array.keys())]
    b = segment[1]
    a = segment[0]
    m = get_candidate_position(segment)
#    import pdb; pdb.set_trace()
    if b - m > 1 :
        diff = b-m
        if diff not in toilet_array:
            toilet_array[diff] = []
        toilet_array[diff].append((m, b))
    if m - a > 1 :
        diff = m-a
        if diff not in toilet_array:
            toilet_array[diff] = []
        toilet_array[diff].append((a, m))

    return best_max, best_min, toilet_array

def get_max_min(toilets, people):
    toilet_array = {toilets : [(-1, toilets)]}
    for i in range(people):
        new_max, new_min, toilet_array = person_enters_toilet(toilet_array)
    return new_max-1, new_min-1

with open('C-small.in') as file:
    with open('output.raw' ,'w') as ofile:
        n = int(file.readline())
        i = 1
        for line in file:
            split_line = line.split()
            toilets = int(split_line[0])
            people = int(split_line[1])
            answer = get_max_min(toilets, people)
            maximum = answer[0]
            minimum = answer[1]
            ofile.write('Case #{}: {} {}\n'.format(i, maximum, minimum))
            i += 1
