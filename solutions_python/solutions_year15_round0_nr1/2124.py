def solve_case(case_num, svals):
    added = 0
    vals_list = list(map(int, svals))
    required = [None] * len(vals_list)
    required[0] = 0
    for i in range(1,len(vals_list)):
        have = sum(vals_list[j] for j in range(i)) + added
        required[i] = max(0, i - have)
        added += required[i]
    print("Case #{}: {}".format(case_num,added))

with open("A-large.in") as f:
    n_cases = int(f.readline().strip())
    for case in range(1,n_cases+1):
        smax, svals = f.readline().strip().split()
        solve_case(case, svals)


