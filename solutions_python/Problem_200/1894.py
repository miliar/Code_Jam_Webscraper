

def findCritical(l):
    critical = -1
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            critical = i
            break
    return critical


def answer(inp):
    l = [int(i) for i in inp]
    critical = findCritical(l)
    if critical == -1:
        return inp
    if l[critical] == 1:
        return "".join(["9" for _ in range(len(l) - 1)])
    firstCritical = critical
    while firstCritical != -1 and l[critical] == l[firstCritical]:
        firstCritical -= 1
    if firstCritical == -1:
        result = [str(l[critical] - 1)]
        result.extend(["9" for _ in range(len(l) - 1)])
        return "".join(result)
    result = list(inp[:firstCritical + 1])
    result.append(str(l[critical] - 1))
    result.extend(["9" for _ in range(firstCritical + 1, len(l) - 1)])
    return "".join(result)


def main():
    numCases = int(input())
    for i in range(numCases):
        print("Case #{}: {}".format(i + 1, answer(input())))


if __name__ == "__main__":
    main()
