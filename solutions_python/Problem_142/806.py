from sys import stdin


input_it = iter(stdin)

T = int(input_it.next())

for t in range(T):

    # interpret input
    # N: number of strings
    # strings: list of strings
    N = int(input_it.next())
    strings = []
    for n in range(N):
        strings.append(input_it.next().rstrip())


    # characters: string of uniq'ed characters that should be in every string
    def characters(s):
        if s == '': return ''
        cs = [s[0]]
        for c in s:
            if c != cs[-1]:
                cs.append(c)
        return ''.join(cs)


    # characters: string of uniq'ed characters that should be in every string
    def occurrences(s):
        # o: occurrences
        # l: last character
        o = []
        l = None
        for c in s:
            if c != l:
                l = c
                o.append(1)
            else: o[-1] += 1
        return o


    y = 0

    # first find out if it is possible at all
    cs = characters(strings[0])
    for i in range(1, N):
        x = characters(strings[i])
        if cs != characters(strings[i]):
            y = 'Fegla Won'
            break

    # if Fegal won, print and continue to next test case
    if y is not 0:
        print 'Case #{x}: {y}'.format(x=t+1, y=y)
        continue

    # then find out how many steps are needed
    occurrences_per_string_per_character = tuple(occurrences(s) for s in strings)
    occurrences_per_character = zip(*occurrences_per_string_per_character)
    total_occurrences = tuple(sum(occs) for occs in occurrences_per_character)
    avg_occurrences = tuple(float(total_occs) / N for total_occs in total_occurrences)
    target_occurrences = tuple(int(round(avg_occs)) for avg_occs in avg_occurrences)

    for real_occs in occurrences_per_string_per_character:
        y += sum(abs(real - target) for (real, target) in zip(real_occs, target_occurrences))

    print 'Case #{x}: {y}'.format(x=t+1, y=y)
