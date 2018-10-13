def standing_ovation(in_name, out_name):
    with open(in_name, 'r') as tests, open(out_name, 'w') as out:
        case = 'Case #{}: {}\n'.format
        for index, test in enumerate(tests):
            if index == 0:
                continue
            groups = (int(a) for a in test.rstrip().split()[1])
            is_standing = 0     # how many people are currently standing
            extra_audience = 0  # how many extra audience members are needed
            for shyness, group in enumerate(groups):
                if shyness > is_standing:
                    diff = shyness - is_standing    # extra people needed
                    is_standing += diff
                    extra_audience += diff
                is_standing += group                # always add total people
            out.write(case(index, extra_audience))  # write answer to file

# standing_ovation('A-small-attempt0.in', 'A-small_output.txt')
standing_ovation('A-large.in', 'A-large_output.txt')
