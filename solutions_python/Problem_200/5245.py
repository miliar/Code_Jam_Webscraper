def is_tidy(str_n):
    nums = [int(x) for x in str_n]
    if len(nums) == 1:
        return True
    if nums[0] <= nums[1]:
        return is_tidy(str_n[1:])
    else:
        return False

def solve(str_n):
    i = int(str_n)
    s = str(i)
    while not is_tidy(s):
        i -= 1
        s = str(i)
    return i

def solve_file(fname):
    with open(fname, 'r') as f:
        values = [x for x in f.readlines()[1:]]
    outname = fname.split('.')[0] + '.out'
    with open(outname, 'w') as of:
        i = 1
        for value in values:
            res = solve(value)
            of.write('Case #{}: {}\n'.format(i, res))
            i += 1
