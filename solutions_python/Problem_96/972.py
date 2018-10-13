import sys

inp = sys.argv[1]
out = sys.argv[2]

def retmax(score, surpr = False):
    if score < 2:
        return score
    if score > 28:
        return 10
    if score % 3 == 0 and not surpr:
        return score / 3
    if score % 3 == 0 and surpr:
        return (score / 3) + 1
    if score % 3 == 1:
        return (score / 3) + 1
    if score % 3 == 2 and not surpr:
        return (score / 3) + 1
    if score % 3 == 2 and surpr:
        return (score / 3) + 2

with open(inp, 'r') as f:
    lines = [[int(i) for i in l.split()] for l in f.readlines()[1:]]
    count = 1
    for line in lines:
        N = line[0]
        S = line[1]
        p = line[2]
        scores = line[3:]
        ans = 0
        for sc in scores:
            if retmax(sc) >= p:
                ans += 1
            elif retmax(sc, True) >= p and S > 0:
                ans += 1
                S -= 1
        with open(out, 'a') as f:
            f.write('Case #{0}: {1}\n'.format(count, ans))
            count += 1



