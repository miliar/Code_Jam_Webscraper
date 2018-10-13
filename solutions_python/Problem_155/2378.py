def standing_ovation():

    number_of_test_cases = int(input())
    test_cases = []
    for _ in range(number_of_test_cases):
        digits = input().split()[-1]
        test_cases.append(digits)

    for i in range(len(test_cases)):
        sum = int(test_cases[i][0])
        invite = 0
        for j in range(1, len(test_cases[i])):
            shyness_level = int(j)
            if shyness_level > sum:
                invite += shyness_level - sum
                sum += shyness_level - sum
            sum += int(test_cases[i][j])
        print('Case #{}: {}'.format(i + 1, invite))


if __name__ == '__main__':
    standing_ovation()
