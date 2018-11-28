def string_to_number(string):
    result = []
    for s in string:
        result.append((int(s)))
    return result


def calculate_result(max_shy_level, string):
    max_shy_level = int(max_shy_level)
    string_numbers = string_to_number(string)
    count = 0
    extra_required = 0
    for i in range(0, max_shy_level + 1):
        if count < i and string_numbers[i] > 0:
            extra_required += i - count
            count += i - count
        count += string_numbers[i]
    return extra_required


def process(case_no):
    max_shy_level, string = raw_input().split()
    result = calculate_result(max_shy_level, string)
    print('Case #{}: {}'.format(case_no, result))

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        process(i + 1)
