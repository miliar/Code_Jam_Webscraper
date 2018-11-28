
def solve(line):
    audience = line.split()[1]
    required = 0
    current = 0
    for i in xrange(len(audience)):
        if audience[i] == 0:
            continue
        if current >= i:
            current += int(audience[i])
        else:
            required += i - current
            current += i - current + int(audience[i])
    return required


if __name__ == "__main__":
    testcases = input()

    for case in xrange(1, testcases+1):
        line = raw_input()
        print("Case #%i: %s" % (case, solve(line)))
