def howManyFriends(shyness_distribution):
    standing = 0
    friends_needed = 0
    for shyness, count in enumerate(shyness_distribution):
        if standing >= shyness:
            standing += count
        else:
            friends_needed_at_this_level = shyness - standing
            friends_needed += friends_needed_at_this_level
            standing += count + friends_needed_at_this_level
    return friends_needed

if __name__ == "__main__":
    import sys
    import os
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        problems = inputfile.readlines()[1:]
    shyness_distributions = map(lambda row: [int(x) for x in row.split()[1]], problems)

    solution_rows = []
    for i, shyness_distribution in enumerate(shyness_distributions):
        solution_rows.append("Case #%s: %s" % (i + 1, howManyFriends(shyness_distribution)))

    with open("solutions/" + os.path.basename(filename) + ".solution", "w+") as solutionfile:
        solutionfile.write("\n".join(solution_rows))
