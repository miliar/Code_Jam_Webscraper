import sys

def recycled_numbers_in_bounds(number, lower_bound, upper_bound):
    num1 = str(number)
    recycled_group = []
    for i in xrange(1, len(num1)):
        recycled = num1[i:] + num1[:i]
        if lower_bound <= int(recycled) <= upper_bound:
            recycled_group.append(int(recycled))
    if recycled_group:
        recycled_group.append(int(num1))
    group = list(set(recycled_group))
    group.sort()
    return group


def possible_combination_tuples_from_list(recycled_list):
    possible_combinations = []
    size = len(recycled_list)
    for smaller_index in xrange(size - 1):
        for larger_index in xrange(smaller_index + 1, size):
            recycled_tuple = (recycled_list[smaller_index], recycled_list[larger_index])
            possible_combinations.append(recycled_tuple)
    return set(possible_combinations)


def get_recycled_numbers_at_interval(A, B):
    recycled_items = set()
    number_of_possible_combinations = 0
    for number in xrange(A, B + 1):
        if number not in recycled_items:
            numbers = recycled_numbers_in_bounds(number, A, B)
            recycled_items = recycled_items.union(set(numbers))
            lenght = len(numbers)
            if lenght > 1:
                number_of_possible_combinations += sum(xrange(lenght))
    return number_of_possible_combinations


def format_output(number, total):
    return "Case #%d: %d\n" % (number, total)


def from_file_to_file(infile, outfile):
    fp_in = open(infile, "r")
    fp_out = open(outfile, "w")
    number_of_lines = int(fp_in.readline().strip())
    for index in xrange(1, number_of_lines + 1):
        line = [int(number) for number in fp_in.readline().strip().split()]
        A = line[0]
        B = line[1]
        answer = get_recycled_numbers_at_interval(A, B)
        fp_out.write(format_output(index, answer))
    fp_in.close()
    fp_out.close()


#import cProfile
#cProfile.run('print get_recycled_numbers_at_interval(100000, 200000)')

# python recycled_numbers.py input.txt output.txt
if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    from_file_to_file(infile, outfile)
