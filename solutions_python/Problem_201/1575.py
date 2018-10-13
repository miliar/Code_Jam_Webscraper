import bisect
import math

IN_FILE = 'C-large'

def solve_exp(N, K):
    space_dict = {N:1}
    space_keys = [N]


    max_s = 0
    min_s = 0

    print('Case #' + str(exp_no + 1) + ': ')

    # shortcut
    # if N > 100:
    #     if K > N/2 + N/10:
    #         return 0, 0
    k = 0
    while k < K:
        space_dict, space_keys, largest, count = get_largest(space_dict, space_keys)

        pos = int(math.ceil(largest / 2.0))

        max_s = largest - pos
        min_s = pos - 1

        # print(str(max_s)+' '+str(min_s)+'--'+str(k))

        space_dict, space_keys = add_space(space_dict, space_keys, max_s, count)
        space_dict, space_keys = add_space(space_dict, space_keys, min_s, count)

        k += count

    return max_s, min_s

def get_largest(space_dict, space_keys):
    largest = space_keys.pop()
    count = space_dict[largest]

    space_dict.pop(largest, None)

    return space_dict, space_keys, largest, count


def add_space(space_dict, space_keys, s, count):
    if s == 0:
        return space_dict, space_keys

    if s in space_dict:
        space_dict[s] += count
    else:
        space_dict[s] = count
        bisect.insort(space_keys, s)

    return space_dict, space_keys


with open(IN_FILE+'.in', 'r') as infile, open(IN_FILE+'.out', 'w') as outfile:

    T = int(infile.readline().strip())

    for exp_no in range(T):
        N, K = map(int, infile.readline().strip().split(' '))

        max_s, min_s = solve_exp(N, K)

        outfile.write('Case #'+str(exp_no+1)+': ')
        outfile.write(str(max_s)+' '+str(min_s)+'\n')
