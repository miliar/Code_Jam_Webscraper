def extra_friends(shyness_levels):
    total_ovations = 0
    friends = 0
    for level, count in enumerate(shyness_levels):
        count = int(count)
        if total_ovations < level and count != 0:
            friends += (level - total_ovations)
            total_ovations += friends
        total_ovations += count
    return friends


if __name__ == '__main__':
    filename = "A-small-attempt0.in"
    output_filename = "ovation_output.txt"
    with open(filename, "r") as f:
        tests_count = f.readline()
        for i, line in enumerate(f):
            max_level, shyness_levels = line.split()
            result = extra_friends(shyness_levels)
            with open(output_filename, "a") as wf:
                wf.write("Case #{0}: {1}\n".format(i + 1, result))
