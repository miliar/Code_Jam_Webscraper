import sys
sys.setrecursionlimit(20000)

DEBUG = True


# def swaps(seq, asc=True):
#     if not asc:
#         seq.reverse()
#     sorted_seq = sorted(seq)
#     indexes = {elem: idx for idx, elem in enumerate(seq)}
#     swaps = 0
#     for idx, sorted_elem in enumerate(sorted_seq):
#         swaps += indexes[sorted_elem] - idx
#         for elem in seq[:indexes[sorted_elem]]:
#             indexes[elem] += 1
#     return swaps
# 
# 
# def solver(n, nums):
#     max_num = max(nums)
#     max_index = nums.index(max_num)
#     best_sort = 10 ** 1000
#     other_nums = nums[:]
#     other_nums.remove(max_num)
#     for i in range(n):
#         swap_count = abs(max_index - i)
#         debug("swap_count for i", i, swap_count)
#         lower = other_nums[:i]
#         try:
#             lower.remove(max_num)
#         except:
#             pass
#         upper = other_nums[i:]
#         try:
#             upper.remove(max_num)
#         except:
#             pass
#         debug("lower", lower)
#         debug("upper", upper)
#         swap_lower = swaps(lower)
#         debug("swap lower", swap_lower)
#         swap_upper = swaps(upper, False)
#         debug("swap upper", swap_upper)
#         swap_count += swap_lower + swap_upper
#         debug("final swap count", swap_count)
#         if swap_count < best_sort:
#             best_sort = swap_count
#     return best_sort

def solver2(n, nums, swaps=0):
    # debug("swaps", swaps)
    # debug("nums", nums)
    if n == 0:
        return swaps
    smallest = min(nums)
    smallest_idx = nums.index(smallest)
    # debug("smallest", smallest, "smallest_idx", smallest_idx)
    swaps += min(smallest_idx - 0, (n - 1) - smallest_idx)
    nums.remove(smallest)
    return solver2(n - 1, nums, swaps)


def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())


def rl():
    return sys.stdin.readline()


def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')


def main():
    # open input file
    # input_file = open('infile.txt')

    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c + 1))
        n = int(rl())
        nums = ssi(rl())
        answer = solver2(n, nums)
        output.append('Case #%d: %s\n' % (c + 1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()


if __name__ == '__main__':
    main()
