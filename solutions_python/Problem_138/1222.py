# Deceitful War
# Submitted for Google Code Jam 2014
# Author: Johnathon Beaumier


def scores(num_blocks, naomis_blocks, kens_blocks):
    """ Solves one test case """

    war_score, war_losses, deceitful_score, deceitful_losses = 0, 0, 0, 0
    naomis_blocks = sorted(naomis_blocks)
    kens_blocks = sorted(kens_blocks)
    assert(num_blocks == len(naomis_blocks) == len(kens_blocks))

    for i in reversed(range(num_blocks)):

        # War:
        #   Naomi strategy: play highest block
        #   Ken strategy: play highest block if he can win, otherwise play lowest
        if float(naomis_blocks[i]) > float(kens_blocks[i + war_score]):
            war_score += 1

        # Deceitful War:
        #   Naomi strategy: play highest block if she can win, otherwise play lowest and say it is just below ken's
        #   Ken strategy: Play highest block to counter Naomi
        if float(naomis_blocks[i + deceitful_losses]) > float(kens_blocks[i]):
            deceitful_score += 1
        else:
            deceitful_losses += 1

    return deceitful_score, war_score


def solve():
    """ Runs through each test case and gives the output """

    file_name = "D-large"
    in_file = open(file_name + ".in", "r")
    out_file = open(file_name + ".out", "w")
    for i, test_case in enumerate(read_test_cases(in_file)):
        n = test_case[0]
        naomi = test_case[1]
        ken = test_case[2]

        line = "Case #{0}: {1} {2}".format(i + 1, *scores(n, naomi, ken))
        record(line, out_file)


def read_test_cases(file):
    """ Collects data for each test case """

    num_test_cases = int(file.readline())
    results = []
    for __ in range(num_test_cases):
        n = int(file.readline())
        naomi = file.readline().split()
        ken = file.readline().split()
        results.append((n, naomi, ken))
    return results


def record(string, file):
    print(string)
    file.write(string + "\n")


solve()