import sys


def possible_numbers(field, choice, prev_numbers=[]):
    if prev_numbers:
        return list(filter(lambda x: x in prev_numbers, field[choice]))
    else:
        return field[choice]

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    cases = int(f.readline())
    for i in range(cases):
        first_answer = int(f.readline()) - 1
        first_field = []
        for _ in range(4):
            first_field.append(list(map(int, f.readline()[:-1].split())))
        second_answer = int(f.readline()) - 1
        second_field = []
        for _ in range(4):
            second_field.append(list(map(int, f.readline()[:-1].split())))
        nums = possible_numbers(first_field, first_answer)
        sec_nums = possible_numbers(second_field, second_answer, nums)
        if len(sec_nums) == 1:
            print("Case #{0}: {1}".format((i+1), sec_nums[0]))
        elif len(sec_nums) > 1:
            print("Case #{0}: {1}".format((i+1), 'Bad magician!'))
        else:
            print("Case #{0}: {1}".format((i+1), 'Volunteer cheated!'))
