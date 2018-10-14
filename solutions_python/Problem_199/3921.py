import sys
import itertools


def flip(pancake, ind):
    n_string = []
    for i, p in enumerate(pancake):
        t = (i >= ind[0]) & (i < ind[1])
        n_string.append(p ^ t)
    return n_string


def window(fseq, window_size=5):
    for i in xrange(len(fseq) - window_size + 1):
        yield (i, i + window_size)


def to_smiles(pancake, k):
    seg = []
    for seq in window(pancake, k):
        seg.append(seq)
    combs = [[]]
    for i in xrange(1, len(seg)+1):
        els = [list(x) for x in itertools.combinations(seg, i)]
        combs.extend(els)
    for comb in combs:
        if all(reduce(flip, comb, pancake)):
            return len(comb)

    return "IMPOSSIBLE"


for i, line in enumerate(sys.stdin):
    if i > 0:
        pancake, k = line.rstrip().split(" ")
        k = int(k)
        pancake = [0 if j == '-' else 1 for j in pancake]
        print "Case #{}: {}".format(
            i,
            to_smiles(pancake, k)
        )
