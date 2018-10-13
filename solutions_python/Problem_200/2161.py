sets = []

with open("/Users/manuel/Desktop/test/codejam/02/B-large.in", "r") as f:
    w = f.read().split("\n")
    for x in range(1, int(w[0]) + 1):
        sets.append(int(w[x]))


def run2(s):
    number = [int(x) for x in list(str(s))]
    inn = inner(number[0], number[1:])
    if inn is not False:
        return [number[0]] + inn
    else:
        return [number[0] - 1] + [9 for i in range(len(number) - 1)]


def inner(prev, number):
    if len(number) == 0:
        return []

    if number[0] >= prev:
        inn = inner(number[0], number[1:])

        if inn is not False:
            return [number[0]] + inn
        else:
            if number[0] - 1 >= prev:
                return [number[0] - 1] + [9 for i in range(len(number) - 1)]
            else:
                return False
    else:
        return False


i = 0
for s in sets:
    i += 1
    print("Case #" + str(i) + ": " + str(int("".join([str(x) for x in run2(s)]))))
