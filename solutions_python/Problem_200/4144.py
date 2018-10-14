
def solve_tidy(n):

    s = str(n)

    res = ""

    i = 0
    while i < len(s):
        a = int(s[i])
        if i == 0 or int(res[i-1]) <= a:
            res += str(a)
            i += 1
        else:
            p = int(res[i-1])
            if res[0] == str(p):
                res = res.replace(str(p), "9")
                res = str(p-1) + res[1:]
            else:
                res = res.replace(str(p), str(p-1))
            res += "9" * len(s[i:])
            break

    return int(res)


if __name__ == '__main__':

    """
    print(solve_tidy(332)) # it was wrong
    print(solve_tidy(120)) # it was wrong
    print(solve_tidy(132))
    print(solve_tidy(1000))
    print(solve_tidy(7))
    print(solve_tidy(111111111111111110))
    exit(0)
    """

    file_base_name = "B-small-attempt3"

    with open(file_base_name+".in", 'rt') as in_file:
        lines = in_file.readlines()

    outlines = []

    for i, line in enumerate(lines[1:]):


        n = int(line)

        sol = solve_tidy(n)

        outlines.append("Case #{}: {}".format(i+1, sol))

    with open(file_base_name+".out", 'wt') as out_file:
        out_file.write("\n".join(outlines))

    print("END")