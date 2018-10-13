import sys


def solve(shyness):
    people_standing = 0
    added_friends = 0

    for i, s in enumerate(shyness):
        if i > people_standing:
            required = i - people_standing
            added_friends += required
            people_standing += required
        people_standing += s

    return added_friends

if __name__ == "__main__":
    file_path = sys.argv[1]
    out_path = file_path + ".out"
    outs = []

    with open(file_path) as fin:
        n = int(fin.readline())
        for line in fin:
            smax, ss = line.strip().split()
            outs.append(solve([int(s) for s in ss]))

    with open(out_path, "w") as fout:
        for i, o in enumerate(outs):
            fout.write("Case #{}: {}\n".format(i + 1, o))
