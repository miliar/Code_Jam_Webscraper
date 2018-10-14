__author__ = 'yulkes'


def read_input_from_file(filename, rows_per_test_case=lambda row: 1): # Rows per test case is a function, receiving the first row
    lines = file(filename).readlines()
    all_cases = []
    curr_case = []
    number_of_total_cases = int(lines[0])
    for line in lines[1:]:
        curr_case.append(line.strip().split(" "))
        if rows_per_test_case(curr_case[0]) >= len(curr_case):  # Make this a new case
            all_cases.append(curr_case)
            curr_case = []
    if all([len(rows) == 1 for rows in all_cases]):
        all_cases = [rows[0] for rows in all_cases]
    assert number_of_total_cases == len(all_cases)
    return all_cases


def process_case(case):
    max_shyness = case[0]
    shy_count = case[1]
    people_to_invite = 0
    standing_so_far = 0
    for shy_level, number_of_people in enumerate(shy_count):
        need_to_invite = 0
        if standing_so_far < shy_level:
            need_to_invite = (shy_level - standing_so_far)
            people_to_invite += need_to_invite
        standing_so_far += int(number_of_people) + need_to_invite
    # Need for each level, to add people so that the number of people in this level >= index of next level
    return str(people_to_invite)


def write_results_to_file(results, filename):
    with file(filename, "w") as out_file:
        for i, res in enumerate(results):
            out_file.write("Case #%d: %s\n" % (i+1, res))

if __name__ == '__main__':
    filename = "A-large.in"
    cases = read_input_from_file(filename)
    results = []
    for case in cases:
        res = process_case(case)
        results.append(res)
    write_results_to_file(results, filename + ".out")