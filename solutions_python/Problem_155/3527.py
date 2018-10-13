def problem_a(infile, outfile):

    with file(infile) as f:
        dat = f.readlines()

    n = int(dat[0])
    assert len(dat[1:]) == n

    test_cases = dat[1:]

    def parse_case(case_text):
        max_val, level_counts = case_text.strip().split()
        max_val, level_counts = int(max_val), [int(x) for x in level_counts]
        return max_val, level_counts

    test_cases = [parse_case(case_text) for case_text in test_cases]

    def find_additional(level_counts):
        total_standing, additional_needed = 0, 0
        for i, n in enumerate(level_counts):
            if total_standing >= i:
                total_standing += n
            else:
                additional_needed += i - total_standing
                total_standing += i -  total_standing + n

        return additional_needed

    with file(outfile, 'wb') as f:
        for case_index, case in enumerate(test_cases):
            max_val, level_counts = case
            res = find_additional(level_counts)
            f.writelines('Case #{0}: {1}\n'.format(case_index + 1, res))