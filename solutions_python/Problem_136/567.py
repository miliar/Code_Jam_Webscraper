import os, sys

def eval_formula(N, (N_precalc, C, F, X)):
    total = N_precalc[N]
    total *= C
    total += float(X - C) / (2 + F * N)
    return total

def do_test_case(ofile, N_precalc, curr_test_case, C, F, X):
    saved_calcs = {}
    data = (N_precalc, C, F, X)

    min_N = 0
    max_N = len(N_precalc)
    check_N = max_N

    # First, make sure it's an upper bound
    top = eval_formula(check_N - 1, data)
    just_under_top = eval_formula(check_N - 2, data)
    if top < just_under_top:
        raise RuntimeException("Bounds set too low!")

    # Start the binary search
    while min_N != max_N:
        check_N = (min_N + max_N) / 2
        if check_N > 0:
            lower = eval_formula(check_N - 1, data)
            equal = eval_formula(check_N, data)
            higher = eval_formula(check_N + 1, data)
            if equal < lower and equal < higher:
                # We've found it
                min_N = max_N = check_N
                break
            elif lower < equal: # Go left
                max_N = check_N - 1
            elif higher < equal: # Go right
                min_N = check_N + 1
            else:
                raise RuntimeException("Branching logic, something's wrong")
        else:
            equal = eval_formula(check_N, data)
            higher = eval_formula(check_N + 1, data)
            if equal < higher:
                min_N = max_N = check_N
                break
            else:
                min_N = check_N + 1
            
    
    bestval = eval_formula(min_N, data)

    print 'Case #%d: %.7f' % (curr_test_case, bestval)
    ofile.write('Case #%d: %.7f' % (curr_test_case, bestval) + "\n")

def main():
    if len(sys.argv) != 3:
        print "Usage: ProblemB.py <input> <output>"
        exit()

    with open(sys.argv[1], 'r') as ifile:
        with open(sys.argv[2], 'w') as ofile:
            ilines = ifile.readlines()
            ncases = int(ilines[0])
            ilines_idx = 1

            for curr_test_case in range(1, ncases + 1):
                [C, F, X] = map(lambda a: float(a), ilines[ilines_idx].split())
                ilines_idx += 1

                range_max = 500000
                N_precalc = list(range(0,range_max))
                total = 0.0
                for n in range(0, range_max):
                    total += 1.0 / (2.0 + F * n)
                    N_precalc[n] = total

                do_test_case(ofile, N_precalc, curr_test_case, C, F, X)

            


if __name__ == "__main__":
    main()
