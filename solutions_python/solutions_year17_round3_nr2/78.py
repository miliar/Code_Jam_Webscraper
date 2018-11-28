num_cases = int(input())

for c in range(num_cases):
    Ac, Aj = map(int, input().split())
    I = []
    for i in range(Ac):
        start, end = map(int, input().split())
        I.append((start, end, 'c'))
    for i in range(Aj):
        start, end = map(int, input().split())
        I.append((start, end, 'j'))

    if Ac + Aj == 0:
        solution = 2
    else:
        I = sorted(I)

        fixed_times = {'c': 0, 'j': 0}
        current = None
        first_person = None
        last_end = I[0][0]
        solution = 0
        merged_free = {'c': [], 'j': []}
        for start, end, person in I:
            if current == person:
                fixed_times[person] += end - last_end
                merged_free[person].append(start - last_end)
            else:
                fixed_times[person] += end - start
                solution += 1
                current = person
                if first_person is None:
                    first_person = person
            last_end = end

        if first_person == person:
            fixed_times[person] += I[0][0] + 1440 - last_end
            merged_free[person].append(I[0][0] + 1440 - last_end)
            solution -= 1

        merged_free['c'] = sorted(merged_free['c'])
        merged_free['j'] = sorted(merged_free['j'])
        while True:
            if fixed_times['c'] > 720:
                solution += 2
                fixed_times['c'] -= merged_free['c'].pop()
            elif fixed_times['j'] > 720:
                solution += 2
                fixed_times['j'] -= merged_free['j'].pop()
            else:
                break

    print('Case #{}: {}'.format(c + 1, solution))
