def read_input(file_name):
    with open(file_name, "r") as fid:
        N = int(fid.readline())
        P = []
        for n in range(N):
            C, F, X = (float(x) for x in fid.readline().split())
            test_case = {
                "C": C,
                "F": F,
                "X": X,
            }
            P.append(test_case)
    return N, P


def solve_problem(P):
    x = 2.0                                 # starting cookie production rate
    tf = lambda x: P["C"] / x               # time to buy a farm
    tx = lambda x: P["X"] / x               # time to end with current cookie production rate
    tz = lambda x: P["X"] / (x + P["F"])    # time to end with cookie production rate after buying a farm
    total_time = 0.
    while tx(x) > (tf(x) + tz(x)):
        total_time += tf(x)
        x += P["F"]
    total_time += tx(x)
    return "%.7f" % total_time

if __name__ == "__main__":
    import os
    path = os.path.realpath(".")
    # file_name = os.path.join(path, "example.in")
    # file_name = os.path.join(path, "B-small-attempt0.in")
    file_name = os.path.join(path, "B-large.in")
    N, P = read_input(file_name)
    with open(file_name[:-2] + "out", "w") as fid:
        for n in range(N):
            solution = solve_problem(P[n])
            fid.write("Case #%d: %s\n" % (n + 1, solution))
    
