def tidy_number(value):
    def tidy_list(input, result):
        if len(input) == 0:
            return result
        elif len(result) == 0:
            return tidy_list(input[:-1], [input[-1]])
        elif result[0] < input[-1]:
            return tidy_list(input[:-1], [input[-1] - 1] + [9] * len(result))
        else:
            return tidy_list(input[:-1], [input[-1]] + result)

    return int(''.join(map(str, tidy_list(map(int, list(value)), []))))


for case in xrange(input()):
    print 'Case #%d: %s' % (case + 1, tidy_number(raw_input()))
