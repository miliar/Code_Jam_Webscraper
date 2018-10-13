from math import ceil, floor

def get_last_val(ppl, max_map):
    while(ppl > 0):
        max_val = max(max_map)
        possible_placements = max_map[max_val]
        # print("loop:", max_map, max_val, possible_placements, ppl)
        if max_val < 1:
            break
        else:
            max_map[max_val] -= ppl
            split_ceil = ceil((max_val - 1) / 2)
            max_map[split_ceil] = max_map.get(split_ceil, 0) + possible_placements
            split_floor = floor((max_val - 1) / 2)
            max_map[split_floor] = max_map.get(split_floor, 0) + possible_placements
            if max_map[max_val] < 1:
                max_map.pop(max_val)
        ppl -= possible_placements

def resolve_case():
    inp = input()
    tiles, ppl = [int(x) for x in inp.split(" ")]
    max_map = {tiles: 1}
    get_last_val(ppl - 1, max_map)
    val = (max(max_map) - 1) / 2
    print(ceil(val), floor(val))
    # print(tiles, ppl, max_map, ceil(val), floor(val), "\n")


cases = int(input())

for case in range(0, cases):
    print("Case #" + str(case + 1), end=": ")
    resolve_case()
