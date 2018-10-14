import sys


def read_input(input_file):
    with open(input_file) as i_f:
        T = int(i_f.readline().strip())
        lines = i_f.readlines()
        for i in range(T):
            s_max, s_counts = lines[i].strip().split()
            s_max = int(s_max)
            s_counts = [int(count) for count in s_counts]
            yield i+1, s_max, s_counts


def solve(s_max, s_counts):
    total = 0
    standing = 0
    friends_needed = 0
    for shyness, people in enumerate(s_counts):
        assert shyness <= s_max
        if standing >= shyness:
            standing += people
        else:
            possible_need = shyness - total - friends_needed
            if possible_need > 0 and people > 0:
                friends_needed += possible_need
        total += people
    return friends_needed


if __name__ == '__main__':
    input_file = sys.argv[1]
    out_file = input_file.replace('.in', '.out')
    with open(out_file, 'w') as o_f:
        for case, s_max, s_counts in read_input(input_file):
            print case
            o_f.write("Case #{}: {}\n".format(case, solve(s_max, s_counts)))
