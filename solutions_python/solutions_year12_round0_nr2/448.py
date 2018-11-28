def max_nonsurprising(total):
    return min((total - 1) / 3 + 1, total)

def max_surprising(total):
    return min((total - 2) / 3 + 2, total)

def max_count_with_given_target(scores, p, num_surprising):
    easy = 0
    hard = 0
    for score in scores:
        if max_nonsurprising(score) >= p:
            easy += 1
        elif max_surprising(score) >= p:
            hard += 1
    #print (easy, hard)
    return easy + min(hard, num_surprising)

infile = open("B-large.in", "r")
outfile = open("B-large.out", "w")

T = int(infile.readline())
for casenum in xrange(1, T+1):
    L = map(int, infile.readline().strip().split())
    N, S, p = L[:3]
    scores = L[3:]
    assert len(scores) == N
    outfile.write("Case #%d: %d\n" % (casenum, max_count_with_given_target(scores, p, S)))

