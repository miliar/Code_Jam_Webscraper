t = int(raw_input())

for i in range(1, t + 1):
    input_str = raw_input()

    list = input_str.split(' ')

    str = list[0]
    k = int(list[1])
    res_str = '+' * len(str)

    total = 0
    stop = True

    all_combinations = set()
    while str != res_str and stop:
        # print 'res {0} {1} = {2}'.format(res_str, str, res_str == str)

        for j in range(k):
            longest = '-' * (k - j)
            replace = '+' * k
            position = str.find(longest)

            if position != -1:
                start_position = position
                if start_position + k > len(str):
                    start_position = len(str) - k

                for index in range(start_position, start_position + k):
                    if str[index] == '+':
                        str = str[0:index] + '-' + str[index + 1:len(str)]
                    else:
                        str = str[0:index] + '+' + str[index + 1:len(str)]

                total += 1

                if str in all_combinations:
                    stop = False

                all_combinations.add(str)

                break

    if not stop:
        print 'Case #{0}: IMPOSSIBLE'.format(i)
    else:
        print 'Case #{0}: {1}'.format(i, total)
