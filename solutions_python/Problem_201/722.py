from __future__ import print_function
import sys
import bisect 
from collections import defaultdict
name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_l_r(largest):
    if largest % 2 == 0:
        l, r = largest // 2 - 1, largest // 2
    else:
        l, r = (largest - 1) // 2 , (largest - 1) // 2
    return l, r

T = int(input())

for testCase in range(1, T + 1):
    n, k = map(int, input().strip().split())
    eprint("case", testCase, n, k)
    A = [n] 
    freq = defaultdict(int) 
    freq[n] = 1
    ppl = k
    while ppl > 0:
        largest = A[-1]
        to_remove = min(freq[largest], ppl)
        #eprint("ppl", ppl, A)
        A = A[:len(A)-1]
        l, r = get_l_r(largest)
        #eprint(largest, "->", l, r)
        for j in [l, r]:
            if j == 0:
                continue
            pos = bisect.bisect_left(A, j)
            if pos >= len(A) or A[pos] != j:
                #eprint("largest", largest, "pos", pos, "j", j, "freq_j", freq[j], "freq_largest", freq[largest])
                bisect.insort(A, j)
            freq[j] += to_remove
        freq[largest] -= to_remove
        ppl -= to_remove
    print("Case #" + str(testCase) + ": " + ("%d %d" % (max(l,r), min(l,r))))
