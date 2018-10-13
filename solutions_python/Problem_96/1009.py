def analyze_triplet(total_score, min_result):
    """
    '+' means its 100% possible
    '*' means its possible, but surprising
    '-' means its impossible
    """
    if total_score == 0:
        if min_result == 0:
            return '+'
        else:
            return '-'

    if total_score >= (min_result * 3 - 2):
        return '+'
    if total_score >= (min_result * 3 - 4):
        return '*'
    return '-'


fin = open("B-large.in")
fout = open("b.out.txt", "w")
for i in xrange(int(fin.readline())):
    x = 0
    data = map(int, fin.readline().split())
    n, s, p = data[:3]
    for t in data[3:]:
        a = analyze_triplet(t, p)
        if a == '+':
            x += 1
        elif a == '*':
            if s > 0:
                x += 1
            s -= 1
    line = "Case #%d: %d" % (i + 1, x)
    print line
    fout.write(line + "\n")

fin.close()
fout.close()