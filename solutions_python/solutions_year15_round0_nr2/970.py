f = open('B-small-attempt0.in', 'r')
outf = open('B-small-attempt0-out.txt', 'w')

P_MIN_MAP = {}
TOTAL_P = 0

T = int(f.readline())

def init_map(pancakes):
    TOTAL_P = sum(pancakes)
    for i in range(1, TOTAL_P + 1):
        P_MIN_MAP['1' * i] = 1
    return TOTAL_P

# def find_max(vec):
#     # find max in a positive vector
#     max_val = 0
#     max_ind = -1
#     for i in range(len(vec)):
#         if vec[i] > max_val:
#             max_val = vec[i]
#             max_ind = i
#     return max_ind, max_val
    
def get_min_minutes(pancakes):
    pancakes.sort()
    p_rep = ''.join(map(str, pancakes))
    if p_rep in P_MIN_MAP:
        return P_MIN_MAP[p_rep]

    max_val = pancakes[-1]
    min_m = TOTAL_P
    for i in range(1, max_val / 2 + 1):
        new_dist = pancakes[:-1] + [i, max_val - i]
        new_time = get_min_minutes(new_dist)
        if new_time < min_m:
            min_m = new_time

    new_dist = [i - 1 for i in pancakes if i -1 > 0]
    new_time = get_min_minutes(new_dist)
    if new_time < min_m:
        min_m = new_time

    P_MIN_MAP[p_rep] = 1 + min_m
    return 1 + min_m

for test_ind in range(T):
    D = int(f.readline())
    pancakes = map(int, f.readline().split())

    TOTAL_P = init_map(pancakes)

    min_m = get_min_minutes(pancakes)

    out_str = 'Case #' + str(test_ind + 1) + ': ' + str(min_m) + '\n'
    outf.write(out_str)

f.close()
outf.close()
        
