import sys
from itertools import combinations, product

def subset_summing_to_zero(activities):
    subsets = {0: []}
    for cost in activities:
        old_subsets = subsets
        subsets = {}
        for (prev_sum, subset) in old_subsets.items():
            subsets[prev_sum] = subset
            new_sum = prev_sum + cost
            new_subset = subset + [cost]
            if 0 == new_sum:
                new_subset.sort()
                return new_subset
            else:
                subsets[new_sum] = new_subset
    return []

def equal_sums(args):
    args = args.split(' ')
    N = int(args[0])
    A = [int(i) for i in args[1:]]
    c = 0
    for d in product([0, -1, 1], repeat=N):
        t = sum(d[i]*A[i] for i in range(N))
        if t == 0:
            if all(i == 0 for i in d): continue
            o = "\n" + ' '.join([str(A[i]) for i in range(N) if d[i] == -1])
            o += "\n" + ' '.join([str(A[i]) for i in range(N) if d[i] == 1])
            return o
    return "Impossible"

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(1, int(Input[0]) + 1):
        args = Input[i]
        result = equal_sums(args)
        Output += "Case #" + str(i) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__": main(sys.argv[1])
