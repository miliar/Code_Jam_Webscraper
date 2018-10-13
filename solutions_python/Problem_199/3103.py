import codecs
from sys import argv

infn = argv[1]
outfn = argv[2]

def get_min_flips(seq, K):
    def flip(seq):
        D = {"+": "-", "-":"+"}
        return [D[symbol] for symbol in seq]
        
    if seq == '+'*len(seq):
        return 0
    num_flips = 0
    seq_l = list(seq)
    while '-' in seq_l:
        modify_loc = seq_l.index("-")
        if modify_loc > len(seq_l) - K:
            return "IMPOSSIBLE"
        seq_l[modify_loc:modify_loc+K] = flip(seq_l[modify_loc:modify_loc+K])     
        num_flips += 1
    return num_flips   

with open(infn, 'r') as f:
    num_cases = int(f.readline().strip())
    cases = [line.strip().split() for line in f.readlines()]
with open(outfn, 'w') as outf:
    cases_written = 0
    for case_num, (sequence, K) in enumerate(cases, start=1):
        K = int(K)
        outf.write("Case #{}: {}\n".format(case_num, get_min_flips(sequence, K)))
        cases_written += 1
    assert cases_written == num_cases
