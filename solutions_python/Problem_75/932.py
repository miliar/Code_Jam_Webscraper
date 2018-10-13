from sys import stdin
import string

raw_data = "".join(stdin.readlines())
test_cases = raw_data.strip().split("\n")[1:]
for test_number, test_string in enumerate(test_cases):
    test_case = test_string.split(" ")
    C = int(test_case.pop(0))
    construction_list = [test_case.pop(0) for i in range(C)]
    constructs = {}
    for i in construction_list:
        constructs[i[0] + i[1]] = i[2]
        constructs[i[1] + i[0]] = i[2]
    D = int(test_case.pop(0))
    contradiction_list = [test_case.pop(0) for i in range(D)]
    contradicts = dict( [(i, []) for i in string.uppercase] )
    for i in contradiction_list:
        contradicts[i[0]].append(i[1])
        contradicts[i[1]].append(i[0])
    N = int(test_case.pop(0))
    series = test_case.pop(0)

    pool = []
    for i in series:
        pool.append(i)
        last_two = "".join(pool[-2:])
        if last_two in constructs:
            pool = pool[:-2]
            pool.append(constructs[last_two])
        else:
            for i in contradicts[pool[-1]]:
                if i in pool:
                    pool = []
    print "Case #%i: [%s]" % (test_number+1, ", ".join(pool))

