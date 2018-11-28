
def get_values(cipher):
    max_level = []
    values = []
    for i, x in enumerate(cipher):
        if x != ' ':
            max_level.append(x)
        else:
            values = cipher[(i+1):]

            break
    values = [int(v) for v in values]
    return int(''.join(max_level)), values


def solve(cipher):
    max_shyness_level, distribution = get_values(cipher)
    num_of_added_friends = 0
    sum_of_input_audience = 0

    for level, value in enumerate(distribution):
        sum_of_audience = sum_of_input_audience + num_of_added_friends
        if sum_of_audience < level:
            num_of_added_friends += level - sum_of_audience
        sum_of_input_audience += value
    return num_of_added_friends


if __name__ == '__main__':
    testcases = input()

    for caseNr in range(1, int(testcases)+1):
        cipher = input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
