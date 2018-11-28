import copy

spelling_map = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
    6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"
}


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def print_ouput():
    lines = getInput("input.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while case <= no_cases:
        sol = get_solution(lines[case].strip())
        print "Case #{0}: {1}".format(case, sol)
        case += 1


def get_solution(input_string):
    input_string = [x for x in input_string.upper()]
    final_numbers = []
    curr_string = copy.deepcopy(input_string)
    count_occurance_map = {
        9: ['E'],
        4: ['I', 'O', 'N'],
        3: ['R', 'T'],
        2: ['F', 'H', 'S', 'V'],
        1: ['G', 'U', 'W', 'X', 'Z']
    }
    one_occurance_map = {"G": 8, "U": 4, "W": 2, "X": 6, "Z": 0}
    curr_string, final_numbers = process_one_occurance_case(count_occurance_map[1], one_occurance_map, curr_string, final_numbers)
    if len(curr_string) == 0:
        return "".join([str(x) for x in sorted(final_numbers)])
    remaining_numbers = [1, 3, 5, 7, 9]
    char_count = {}
    for num in spelling_map:
        if num in remaining_numbers:
            for char in spelling_map[num]:
                char_count[char] = char_count.get(char, 0) + 1
    count_occurance_map = {}
    for char, count in char_count.items():
        count_occurance_map.setdefault(count, []).append(char)
    count_occurance_map = {
        1: ['F', 'H', 'O', 'S', 'R', 'T'],
        2: ['I', 'V'],
        4: ['N'],
        7: ['E']
    }
    one_occurance_map = {}
    for char in count_occurance_map[1]:
        for num in remaining_numbers:
            if char in spelling_map[num]:
                one_occurance_map[char] = num
                break
    one_occurance_map = {'F': 5, 'H': 3, 'O': 1, 'S': 7, 'R': 3, 'T': 3}
    curr_string, final_numbers = process_one_occurance_case(count_occurance_map[1], one_occurance_map, curr_string, final_numbers)
    if len(curr_string) == 0:
        return "".join([str(x) for x in sorted(final_numbers)])
    else:
        curr_string, final_numbers = process_9_case(curr_string, final_numbers)
    if len(curr_string) == 0:
        return "".join([str(x) for x in sorted(final_numbers)])


def process_9_case(curr_string, final_numbers):
    count_n = len([x for x in curr_string if x == "N"])
    if count_n % 2 == 0:
        for loop in xrange(0, count_n/2):
            final_numbers.append(9)
            for each_char in spelling_map[9]:
                curr_string.remove(each_char)
    return curr_string, final_numbers


def process_one_occurance_case(one_occurance_list, one_occurance_map, curr_string, final_numbers):
    for char in one_occurance_list:
        number = one_occurance_map[char]
        count = len([x for x in curr_string if x == char])
        for loop in xrange(0, count):
            final_numbers.append(number)
            for each_char in spelling_map[number]:
                curr_string.remove(each_char)
    return curr_string, final_numbers


def get_occurance_count(input_str, find_char):
    len([x for x in input_str if x == find_char])



print_ouput()