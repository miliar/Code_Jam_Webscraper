
def problem_solve(N, P, groups):

    mods = {i : 0 for i in range(P)}
    for g in groups:
        mods[g % P] += 1

    sol = 0

    sol += mods[0]
    if P == 2:
        sol += (mods[1] + 1) / 2
    if P == 3:
        a = min(mods[1], mods[2])
        sol += a
        rest = max(mods[1], mods[2]) - a
        sol += (rest + 2) / 3
    if P == 4:
        res_2 = 0
        if mods[2] % 2 == 1:
            res_2 += 1
        mods[2] -= 1
        sol += mods[2] / 2
        a = min(mods[1], mods[2])
        sol += a
        rest = max(mods[1], mods[3]) - a
        if rest >= 2 and res_2 == 1:
            sol += 1
            rest -= 2
        sol += (rest + 3) / 4
    
    
    return sol

def problem_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        N = int(inputs[0])
        P = int(inputs[1])
        groups = [int(x) for x in f.readline().split()]


        #print N, horse_cap, horse_speed, edges, targets
        sol = problem_solve(N, P, groups)
        str_sol = " ".join([str(x) for x in [sol]])
        output_f.write("Case #" + str(i) + ": " + str_sol + "\n")
    return 1

problem_main("A-small-attempt0.in", "A-small-attempt0.out")
