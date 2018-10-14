import sys
import math


def max_matching(packs):
    tot = 0
    while len(packs[0]) > 0:
        cand_range = [packs[0].pop()]
        cur_pack = 1
        cur_range = cand_range[:]
        while 0 < cur_pack < len(packs):
            if len(packs[cur_pack]) == 0:
                return tot
            cur_range = cand_range[-1]
            cand_match = packs[cur_pack][-1]
            if cand_match[0] > cur_range[1]:
                packs[cur_pack].pop()
                continue
            if cand_match[1] < cur_range[0]:
                cand_range.pop()
                cur_pack -= 1
            else:
                packs[cur_pack].pop()
                new_range = [None, None]
                new_range[0] = max(cur_range[0], cand_match[0])
                new_range[1] = min(cur_range[1], cand_match[1])
                cur_pack += 1
                cand_range.append(new_range)    
        if cur_pack == len(packs):
            tot += 1    
    return tot    

def range_packs(val, per_pack):
    low = (100*val)/(110*per_pack)
    low = max(math.ceil(low), 1)
    hi = (100*val)/(90*per_pack)
    hi = math.floor(hi)
    if hi < low:
        return None
    return low, hi

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        num_ing, num_pack = (int(val) for val in in_file.readline().strip().split())
        #Call func for solution
        recipe = [int(val) for val in in_file.readline().strip().split()]
        packs = []
        for index in range(num_ing):
            cand = [int(val) for val in in_file.readline().strip().split()]
            cand.sort()
            to_add = []
            for val in cand:
                val_packs = range_packs(val, recipe[index])
                if val_packs is not None:
                    to_add.append(val_packs)
            packs.append(to_add)
        sol = max_matching(packs)
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'B-sample'
        #name = 'B-small-attempt0'
        name = 'B-large'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
