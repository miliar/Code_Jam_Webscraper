import codejam


specifier = codejam.CaseSpecifier(
    codejam.ArgumentSpecifier("s_max", arg_type=int),
    codejam.ArgumentSpecifier("first_list", arg_type=int, is_list=True),
    specified_on_one_line=True
)

test_input = """4
4 11111
1 09
5 110011
0 1"""


test_output = """Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0"""


def solve(case):
    n_friends_to_bring = 0
    cur_standing = 0

    for people_required, n_people_at_level in enumerate(case["first_list"]):
        if people_required > cur_standing + n_friends_to_bring:
            n_friends_to_bring += (people_required - cur_standing - n_friends_to_bring)

        cur_standing += n_people_at_level

    return codejam.Answer(n_friends_to_bring)




problem = codejam.Problem(test_input, test_output, specifier, solve)
problem.large_run()