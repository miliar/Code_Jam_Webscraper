def solve(f):
    N = int(f.readline())
    words = [f.readline() for i in xrange(N)]
    decomp = []
    for i, w in enumerate(words):
        l, c = '', 0
        decomp.append([])
        while w:
            if not l:
                l = w[0]
                c = 0
            if l != w[0]:
                decomp[i].append((l, c))
                l = w[0]
                c = 0
            c += 1
            w = w[1:]
    letters = [d[0] for d in decomp[0]]
    for d in decomp[1:]:
        if [tup[0] for tup in d] != letters:
            return "Fegla Won"
    ideal_string = [0] * len(decomp[0])
    for d in decomp:
        for i, (l, c) in enumerate(d):
            ideal_string[i] += c
    ideal_string = [x/len(decomp) for x in ideal_string]
    moves = 0
    for d in decomp:
        for i, (l, c) in enumerate(d):
            moves += abs(ideal_string[i] - c)
    return str(moves)


test_answer = {
    1: "1",
    2: "Fegla Won",
    3: "4",
    4: "0",
    5: "3",
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
