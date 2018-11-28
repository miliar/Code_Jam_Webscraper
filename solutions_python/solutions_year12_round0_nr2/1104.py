import sys

NOT_SURPRISING = 2
SURPRISING = 1
WILL_NEVER_HAPPEN = 0

total_points = lambda score_triple: sum(score_triple)
best_result = lambda score_triple: max(score_triple)


def positive_difference(num1, num2):
    diff = num1 - num2
    if diff > 0:
        return diff
    return -1 * diff


def largest_difference(score_triple):
    num1, num2, num3 = score_triple
    diff_list = [\
        positive_difference(num1, num2),
        positive_difference(num1, num3),
        positive_difference(num2, num3)]
    return max(diff_list)


def check_triple_type(score_triple):
    largest_diff = largest_difference(score_triple)
    if largest_diff < 2:
        return NOT_SURPRISING
    elif largest_diff == 2:
        return SURPRISING
    else:
        return WILL_NEVER_HAPPEN


def max_score_from_list_of_triples(triples_list):
    best = 0
    for triple in triples_list:
        best_of_triple = best_result(triple)
        if best_of_triple > best:
            best = best_of_triple
    return best


def possible_triples(score, p):
    average = score / 3
    min_value = average - 2
    if min_value < 0:
        min_value = 0
    max_value = average + 3
    if max_value > 11:
        max_value = 11
    combinations = []
    type_of = 0
    for item1 in xrange(min_value, max_value):
        for item2 in xrange(min_value, max_value):
            for item3 in xrange(min_value, max_value):
                if (item1 + item2 + item3) == score:
                    type_this = check_triple_type([item1, item2, item3])
                    if type_this and max([item1, item2, item3]) >= p:
                        combinations.append([item1, item2, item3])
                        if type_this > type_of:
                            type_of = type_this
    return combinations, type_of


def reply_to_question(list_of_numbers, surprise, p):
    total = 0
    used_surprises = 0

    for i in xrange(len(list_of_numbers)):
        possibles_item, type_of_item = possible_triples(list_of_numbers[i], p)
        max_item = max_score_from_list_of_triples(possibles_item)
        if max_item >= p:
            if type_of_item == 2:
                total += 1
            elif type_of_item == 1:
                if used_surprises < surprise:
                    used_surprises += 1
                    total += 1
    return total


def format_output(number, total):
    return "Case #%d: %d\n" % (number, total)


def from_file_to_file(infile, outfile):
    fp_in = open(infile, "r")
    fp_out = open(outfile, "w")
    number_of_lines = int(fp_in.readline().strip())
    for index in xrange(1, number_of_lines + 1):
        line = [int(number) for number in fp_in.readline().strip().split()]
        surprise = line[1]
        p = line[2]
        list_of_numbers = line[3:]
        answer = reply_to_question(list_of_numbers, surprise, p)
        fp_out.write(format_output(index, answer))
    fp_in.close()
    fp_out.close()

# python dancing_with_the_googlers.py dancing_with_the_googlers_input.txt dancing_with_the_googlers_my_output.txt
if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    from_file_to_file(infile, outfile)
