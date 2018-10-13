import sys

def main():
    stdinlines = sys.stdin.readlines()
    for i in range(len(stdinlines)):
        stdinlines[i] = stdinlines[i].strip() 

    testCases = []

    nrTestCases = int(stdinlines.pop(0))
    #print("Test cases: {0}".format(nrTestCases))

    if nrTestCases != len(stdinlines):
        print("Error: the number of test cases did not match the number of"
            " input lines.")
        return 1

    for line in stdinlines:
        print(line)
        parts = line.partition(' ')
        testCases.append((int(parts[0]), int(parts[2])))

    i = 1
    for testCase in testCases:
        #print("Running test case {0}".format(i))
        result = run_test_case(testCase[0], testCase[1])
        print("Case #{0}: {1}".format(i, 'ON' if result else 'OFF'))
        i += 1

    return 0

def run_test_case(n, k):
    snappers = [False for i in range(n)]

    for i in range(k):
        for snapper in range(len(snappers)):
            oldValue = snappers[snapper]
            snappers[snapper] = not snappers[snapper]
            if not oldValue:
                break

    #print(snappers)

    for snapper in snappers:
        if not snapper:
            return False

    return True

if __name__ == '__main__':
    sys.exit(main())


