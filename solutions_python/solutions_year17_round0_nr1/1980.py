
def flip(pattern, index, flip_mask):
    mask = flip_mask << index
    return pattern^mask

def pancace_flip_count(pattern, flip_mask, comb_count, min_ittr, itter=0):
    for flip_index in range(1, comb_count+1):
        min_ittr[pattern] = itter
        next_pattern = flip(pattern, flip_index-1, flip_mask)
        if (next_pattern not in min_ittr) or (min_ittr[next_pattern] > itter):
            pancace_flip_count(next_pattern, flip_mask, comb_count, min_ittr, itter+1)
        else:
            break


def resolve_case():
    inp = input()
    pattern, flip_size = inp.split(" ")
    pattern = ['0' if x == '+' else '1' for x in list(pattern)]
    flip_size = int(flip_size)
    count = len(pattern)
    min_ittr = {}
    num = int(''.join(pattern), 2)
    pancace_flip_count(num, int('1'*flip_size, 2), len(pattern) - flip_size + 1, min_ittr)
    print(min_ittr.get(0, "IMPOSSIBLE"))



cases = int(input())

for case in range(0, cases):
    print("Case #" + str(case + 1), end=": ")
    resolve_case()
