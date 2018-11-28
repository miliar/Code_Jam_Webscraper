def and_with_list(k, num, b):
    for n in b:
        if num & n < k:
            yield 1

def answer(input_string):
    in_lines = input_string.splitlines()
    t, cases = in_lines[0], in_lines[1:]
    cases_split = map(lambda x: x.split(), cases)
    for i, case in enumerate(cases_split):
        count = 0
        a, b, k = int(case[0]), int(case[1]), int(case[2])
        l = min([a, b])
        q = max([a, b])
        li = range(l)
        lq = range(q)
        for num in xrange(l):
            count += sum(and_with_list(k, num, lq))
        print 'Case #{0}: {1}'.format(i + 1, count)
