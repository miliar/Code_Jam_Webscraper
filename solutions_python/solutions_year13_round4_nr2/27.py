from collections import Counter

def solve1(N, P):

    if P == 1: return 0
    if P == (2 ** N): return P-1

    R = 0
    b = N-1
    while P >  0:
        R += 1
        P -= 2 ** b
        b -= 1

    return (2 ** R) - 2


def solve2(N, P):

    if P == 1: return 0
    if P == (2 ** N): return P-1

    R = N
    while P > 1:
        R -= 1
        P /= 2
    #print R
    effort = (2 ** R) - 1

    #print 2**N, effort

    return (2 ** N) - effort - 1

if __name__ == '__main__':

    import sys
    
    input_file = sys.argv[1]
    output_file = input_file[:].replace('.in', '.out')


    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')

    T, = [int(x) for x in f_in.readline().split()]

    for case in range(1, T+1):
        print 
        print '====================='
        print '    ' + str(case)
        print '====================='

        N, P = [int(x) for x in f_in.readline().split()]

        # Solve
        ans1 = solve1(N, P)
        ans2 = solve2(N, P)

        print ans1, ans2

        ## Output
        f_out.write('Case #%d: %s %s\n' % (case, ans1, ans2))

        

