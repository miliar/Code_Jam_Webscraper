__author__ = 'yulkes'


def read_input_from_file(filename, rows_per_test_case=lambda row: 1): # Rows per test case is a function, receiving the first row
    lines = file(filename).readlines()
    all_cases = []
    curr_case = []
    number_of_total_cases = int(lines[0])
    for line in lines[1:]:
        curr_case.append(line.strip().split(" "))
        if rows_per_test_case(curr_case[0]) == len(curr_case):  # Make this a new case
            all_cases.append(curr_case)
            curr_case = []
    if all([len(rows) == 1 for rows in all_cases]):
        all_cases = [rows[0] for rows in all_cases]
    assert number_of_total_cases == len(all_cases)
    return all_cases

cache = {}

def minimum_minutes(plates):
    filled_plates = sorted(p for p in plates if p)
    key = tuple(filled_plates)
    if key not in cache:
        if max(plates) == 1:
            return 1
        if max(plates) == 0:
            return 0

        biggest_plate = max(plates)
        index_of_max = plates.index(biggest_plate)
        possibilities = []
        for i in range(1, biggest_plate / 2 + 1):
            option = plates[:]
            option[index_of_max] -= i
            option.append(i)
            possibilities.append(option)

        min_minutes = min(1 + minimum_minutes([p-1 for p in plates if p]), *[1 + minimum_minutes(option) for option in possibilities])
        cache[key] = min_minutes
    return cache[key]

def process_case(case):
    pancakes_for_plate = [int(p) for p in case[1]]
    minutes = minimum_minutes(pancakes_for_plate)
    return str(minutes)

def write_results_to_file(results, filename):
    with file(filename, "w") as out_file:
        for i, res in enumerate(results):
            out_file.write("Case #%d: %s\n" % (i+1, res))

if __name__ == '__main__':
    filename = "B-small-attempt1.in"
    cases = read_input_from_file(filename, lambda row: 2)
    results = []
    for i, case in enumerate(cases):
        print "Working on %d: %s" % (i, case)
        res = process_case(case)
        results.append(res)
    write_results_to_file(results, filename + ".out")