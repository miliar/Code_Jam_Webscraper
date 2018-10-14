def solve(input):
    N = int(input.readline())
    Naomi = sorted(map(float, input.readline().split()))
    DNaomi = Naomi[:]
    Ken = sorted(map(float, input.readline().split()))
    DKen = Ken[:]
    deceitful_score = 0
    legal_score = 0
    for i in xrange(N):
        #print "Naomi %s" % Naomi
        #print "Ken %s" % Ken
        #print "legal score %d" % legal_score
        legal_score += play_legal(Naomi, Ken)
        #print "DNaomi %s" % DNaomi
        #print "DKen %s" % DKen
        #print "deceitful score %s" % deceitful_score
        deceitful_score += play_deceitful(DNaomi, DKen)
    #print "%d %d" % (deceitful_score, legal_score)
    return "%d %d" % (deceitful_score, legal_score)

def play_legal(Naomi, Ken):
    N = Naomi.pop()
    if N > Ken[-1]:
        Ken.pop(0)
        return 1
    for i, k in enumerate(Ken):
        if k > N:
            Ken.pop(i)
            return 0

def play_deceitful(Naomi, Ken):
    K = Ken.pop(0)
    if K > Naomi[-1]:
        Naomi.pop(0)
        return 0
    for i, n in enumerate(Naomi):
        if n > K:
            Naomi.pop(i)
            return 1

test_answer = {
    1: "0 0",
    2: "1 0",
    3: "2 1",
    4: "8 4",
}

if __name__ == '__main__':
    import sys
    test = False
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = 'test.txt'
        test = True
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    with open(file_name) as f:
        T = int(f.readline())
        for i in range(1, T + 1):
            answer = solve(f)
            if test:
                assert answer == test_answer[i]
            else:
                print "Case #%d: %s" % (i, answer)
