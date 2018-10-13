def read_input(file_name):
    with open(file_name, "r") as fid:
        N = int(fid.readline())
        P = []
        for n in range(N):
            fid.readline()
            test_case = {
                "Naomi": [float(x) for x in fid.readline().split()],
                "Ken": [float(x) for x in fid.readline().split()]
            }
            P.append(test_case)
    return N, P


def kens_strategy(ken, naomis_choice):
    for n in range(len(ken)):
        if ken[n] > naomis_choice:
            # returns first heavier object on sorted list
            return ken.pop(n)
    # have no heavier element, returns lightest
    return ken.pop(0)


def naomis_strategy_standard(naomi):
    return naomi.pop(-1)


def naomis_strategy_deceitful(naomi, ken):
    for n in range(len(naomi)):
        if naomi[n] > ken[0]:
            naomi_chose = naomi.pop(n)
            naomi_tell = ken[-1] + 0.05
            return naomi_tell, naomi_chose
    naomi_chose = naomi_tell = naomi.pop(-1)
    return naomi_tell, naomi_chose


def solve_problem(P):
    P["Naomi"].sort()
    P["Ken"].sort()

    # playing Deceitful War
    K = P["Ken"][:]
    N = P["Naomi"][:]
    score_deceitful = 0
    while len(K) > 0:
        n_told, n_chose = naomis_strategy_deceitful(N, K)
        k = kens_strategy(K, n_told)
        if n_chose > k:
            score_deceitful += 1

    # playing War
    K = P["Ken"][:]
    N = P["Naomi"][:]
    score_standard = 0
    while len(K) > 0:
        n = naomis_strategy_standard(N)
        k = kens_strategy(K, n)
        if n > k:
            score_standard += 1
    return "%d %d" % (score_deceitful, score_standard)


if __name__ == "__main__":
    import os
    path = os.path.realpath(".")
    # file_name = os.path.join(path, "example.in")
    # file_name = os.path.join(path, "D-small-attempt0.in")
    file_name = os.path.join(path, "D-large.in")
    N, P = read_input(file_name)
    with open(file_name[:-2] + "out", "w") as fid:
        for n in range(N):
            solution = solve_problem(P[n])
            fid.write("Case #%d: %s\n" % (n + 1, solution))