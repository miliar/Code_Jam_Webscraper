def min_max(size, tries):
    consecutive = [size]
    while tries > 0:
        choosed = consecutive[0] - 1
        consecutive = consecutive[1:]
        repeat = 0
        for available in consecutive:
            if available == choosed + 1:
                repeat += 1
            elif available < choosed:
                break
        if repeat >= tries:
            tries = 0
        else:
            tries -= repeat
            consecutive = [x for x in consecutive if x != choosed + 1]
            # print(consecutive)
        if choosed == 0:
            min_s = max_s = 0
            tries -= 1
            continue
        elif choosed % 2:
            max_s = choosed / 2 + 0.5
            min_s = choosed / 2 - 0.5
        else:
            min_s = max_s = choosed / 2
        for value in [int(max_s), int(min_s)]:
            if value:
                for _ in range(0, repeat+1):
                    consecutive.append(value)
        consecutive.sort(reverse=True)
        tries -= 1
    # print(consecutive)
    return int(max_s), int(min_s)

c_num = int(input())
cases = []
for i in range(0, c_num):
    cases.append(input())
for i in range(0, c_num):
    stall, person = cases[i].split()
    max_r, min_r = min_max(int(stall), int(person))
    print("Case #%d: %s %s" % ((i+1), max_r, min_r))

