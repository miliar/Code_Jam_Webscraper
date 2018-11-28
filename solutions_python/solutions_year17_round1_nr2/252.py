from collections import defaultdict
import sys

def subsolve(n, right, pairs):
    if n == -1:
        return 0
    taken = 0
    for r in right:
        if r in pairs[0][n][1]:
            attempt = 1 + subsolve(n-1, [_ for _ in right if _ != r], pairs)
            if attempt > taken:
                taken = attempt
    attempt = subsolve(n-1, right, pairs)
    if attempt > taken:
        taken = attempt
    return taken

def solve(n, serving_amounts, packages):
    if n == 1:
        serving_amount = serving_amounts[0]
        retval = 0
        for p in packages[0]:
            servings = round(float(p) / serving_amount)
            min_amount = .9 * servings * serving_amount
            max_amount = 1.1 * servings * serving_amount
            if min_amount <= p <= max_amount:
                retval += 1
        return retval
    pairs = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    for left, lst in enumerate(packages):
        for left_index, amount in enumerate(lst):
            base_servings = round(float(amount) / serving_amounts[left])
            max_diff = int(base_servings*1.2)
            for ds in range(-max_diff-1, max_diff+2):
                servings = base_servings + ds
                min_amount = .9 * servings * serving_amounts[left]
                max_amount = 1.1 * servings * serving_amounts[left]
                if servings <= 0 or not(min_amount <= amount <= max_amount):
                    continue
                for right, lst_right in enumerate(packages):
                    if left != right:
                        min_amount = .9 * servings * serving_amounts[right]
                        max_amount = 1.1 * servings * serving_amounts[right]
                        for right_index, right_amount in enumerate(lst_right):
                            if min_amount <= right_amount <= max_amount:
                                pairs[left][left_index][right].add(right_index)
    #print pairs
    assert(n == 2)
    p = len(packages[0])
    return subsolve(p-1, list(range(p)), pairs)


t = int(next(sys.stdin))
for test in range(t):
    n, p = [int(s) for s in next(sys.stdin).strip().split(' ')]
    assert(n <= 2)
    assert(p <= 8)
    servings = [int(s) for s in next(sys.stdin).strip().split(' ')]
    packs = []
    for _ in range(n):
        packs.append([int(s) for s in next(sys.stdin).strip().split(' ')])
    print('Case #{}: {}'.format(test+1, solve(n, servings, packs)))
