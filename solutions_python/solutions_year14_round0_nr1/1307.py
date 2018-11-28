def read_input(file_name):
    with open(file_name, "r") as fid:
        N = int(fid.readline())
        P = []
        for n in range(N):
            test_case = {
                "1st Answer": int(fid.readline()) - 1,
                "1st Cards": [[int(x) for x in fid.readline().split()] for _ in range(4)],
                "2nd Answer": int(fid.readline()) - 1,
                "2nd Cards": [[int(x) for x in fid.readline().split()] for _ in range(4)]
            }
            P.append(test_case)
    return N, P


def solve_problem(P):
    cards = list(set(P["1st Cards"][P["1st Answer"]]) & set(P["2nd Cards"][P["2nd Answer"]]))
    if len(cards) == 0:
        return "Volunteer cheated!"
    elif len(cards) == 1:
        return "%d" % cards[0]
    else:
        return "Bad magician!"


if __name__ == "__main__":
    import os
    path = os.path.realpath(".")
    file_name = [
        os.path.join(path, "example.in"),
        os.path.join(path, "A-small-attempt0.in"),
        os.path.join(path, "A-large-practice.in")
    ]
    which = 1
    N, P = read_input(file_name[which])
    with open(file_name[which][:-2] + "out", "w") as fid:
        for n in range(N):
            solution = solve_problem(P[n])
            fid.write("Case #%d: %s\n" % (n + 1, solution))

