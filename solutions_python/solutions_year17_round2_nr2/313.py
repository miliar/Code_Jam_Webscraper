import string

def solve_small(N, R, Y, B):
    # let S <= M <= L be a remapping
    S = min(R, Y, B)
    L = max(R, Y, B)
    M = R + Y + B - S - L

    print S, M, L

    if S + M - L < 0:
        return "IMPOSSIBLE"
    if S == R:
        S_color = "R"
        if M == Y:
            M_color = "Y"
            L_color = "B"
        else:
            L_color = "Y"
            M_color = "B"
    elif S == Y:
        S_color = "Y"
        if M == R:
            M_color = "R"
            L_color = "B"
        else:
            M_color = "B"
            L_color = "R"
    elif S == B:
        S_color = "B"
        if M == R:
            M_color = "R"
            L_color = "Y"
        else:
            M_color = "Y"
            L_color = "R"
    else:
        print "error!"
        exit(1)

    print L_color, M_color, S_color

    LMS = L_color + M_color + S_color
    LM = L_color + M_color
    LS = L_color + S_color

    return LMS*(S+M-L) + LM*(L-S) + LS*(L-M)

def solve_large(N, R, O, Y, G, B, V):
    # O requires BOB
    # G requires RGR
    # V requires YVY
    pass


def test(inputs, ans):
    b = solve(*inputs)
    if (b != ans):
        print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))

    for k in xrange(1,T+1):
        print k
        N, R, O, Y, G, B, V = map(int,string.strip(raw_input()).split())
        # parse the line here
        if O == 0 and G == 0 and V == 0:
            answer = solve_small(N, R, Y, B)
        else:
            answer = solve_large(N, R, O, Y, G, B, V)

        outfile.write('Case #%d: %s\n' % (k,answer))

if __name__ == '__main__':
    main()
