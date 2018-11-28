FILE = "al.in"
OUT = "out_"+FILE


def parse(filepath):
    f = open(filepath)
    lines = [l.strip() for l in f.readlines()]
    f.close()
    print lines
    return lines


def saveResult(results):
    formatted = ["Case #{0}: {1}".format(k+1, v) for k, v in enumerate(results)]
    formatted = '\n'.join(formatted)
    f = open(OUT, 'w+')
    f.write(formatted)
    f.close()


def problemA(lines):
    results = [problemASingleCase(l) for l in lines]

    return results


def problemASingleCase(line):
    result = 0
    data = [int(i) for i in list(line.split()[1])]

    if not 0 in data:
        return 0

    for k, v in enumerate(data):
        s = sum(data[:k]) + result

        
        if v == 0 and s < k+1:
            result += k+1 - s

    # if data[0] == 0:
    #     result += 1

    return result


answer = problemA(parse(FILE)[1:])
print answer

saveResult(answer)
