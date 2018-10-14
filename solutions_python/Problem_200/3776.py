def is_correct(number):
    if len(number) == 1:
        return -1

    # print 'process {0}'.format(number)
    for i in range(0, len(number) - 1):
        if int(number[len(number) - 2 - i]) > int(number[len(number) - 1 - i]):
            return len(number) - 2 - i

    return -1

t = int(raw_input())

for i in range(1, t + 1):
    number = raw_input()
    # print number

    is_valid = False
    index = 0
    while index >= 0:
        index = is_correct(number)
        # print 'index {0}'.format(index)

        if index == -1:
            break

        if index == 0:
            dec_numb = int(number[index]) - 1
            number = '{0}'.format(dec_numb) + '9' * (len(number) - 1)
        else:
            dec_numb = int(number[index]) - 1
            number = number[0:index] + '{0}'.format(dec_numb) + '9' * (len(number) - index - 1)

        # print 'modified {0}'.format(number)

    print 'Case #{0}: {1}'.format(i, int(number))

    # if not stop:
    #     print 'Case #{0}: IMPOSSIBLE'.format(i)
    # else:
    #     print 'Case #{0}: {1}'.format(i, total)

