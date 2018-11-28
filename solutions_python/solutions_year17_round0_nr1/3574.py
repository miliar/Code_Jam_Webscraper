from collections import Counter


def splitter(value):
    l = value.split(' ')
    return l[0], int(l[1])


def count_happy(pankakes):
    happy = '+'

    if pankakes != '':
        total = Counter(pankakes)
        if total[happy] == len(pankakes):
            return True
    return False


def is_even(num):
    return num % 2


def worker(in_values):

    not_happy = '-'
    pancakes, pan = splitter(in_values)

    if count_happy(pancakes):
        return 0
    total = 0
    for i in range(len(pancakes)):
        if pancakes[i] == not_happy:
            if i + pan > len(pancakes) and not count_happy(pancakes):
                return 'IMPOSSIBLE'
            pancakes = replace(pancakes, i, pan)
            total += 1
        if count_happy(pancakes):
            return total


def replace(pancakes, from_pos, times):
    if from_pos + times > len(pancakes):
        return pancakes

    str_list = list(pancakes)

    while times > 0:
        if str_list[from_pos] == '+':
            str_list[from_pos] = '-'
        else:
            str_list[from_pos] = '+'
        from_pos += 1
        times -= 1
    return "".join(str_list)


if __name__ == '__main__':
    # test = int(input())
    #
    # t = 1
    # while t <= test:
    #     in_value = input()
    #     print("Case #{}: {}".format(t, worker(in_value)))
    #     t += 1

    with open('/Users/lobanod/PycharmProjects/GoogleJam/Qualification/output.txt', 'w') as output:

        with open('/Users/lobanod/PycharmProjects/GoogleJam/Qualification/test.txt', 'r') as file:
            test = int(file.readline())
            t = 1
            for f in file.readlines():
                print("Case #{}: {}".format(t, worker(f)))
                #file.write("Case #{}: {}".format(t, worker(f)))
                t += 1
