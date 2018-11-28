
def solve_pancake(S, K):

    count = 0
    while K <= len(S):
        first = S.find("-")
        if first == -1:
            S = ""
        elif first == 0:
            count += 1
            S = "".join(["+" if s == "-" else "-" for s in S[:K]]) + S[K:]
        else:
            S = S[first:]

    return count if S == "" else "IMPOSSIBLE"


if __name__ == '__main__':

    """
    print(solve_pancake("---+-++-", 3))
    #print(solve_pancake("+++++", 4))
    #print(solve_pancake("-+-+-", 4))
    exit(0)
    """

    #file_base_name = "A-small-attempt0"
    file_base_name = "A-large"

    with open(file_base_name+".in", 'rt') as in_file:
        lines = in_file.readlines()

    outlines = []

    for i, line in enumerate(lines[1:]):

        splitted_line = line.split(" ")
        S = splitted_line[0]
        K = int(splitted_line[1])

        sol = solve_pancake(S, K)

        outlines.append("Case #{}: {}".format(i+1, sol))

    with open(file_base_name+".out", 'wt') as out_file:
        out_file.write("\n".join(outlines))

    print("END")