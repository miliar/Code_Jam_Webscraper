import sys

numTests = int(sys.stdin.readline())
tests = []

# Read all tests
for i in range(numTests):
    t = sys.stdin.readline()
    tests.append(t)

# Solve them
for i in range(numTests):
    numberString = list(tests[i][:-1])
    number = [int(x) for x in numberString]

    point = 0
    for j in range(len(number)-1):
        if number[j] > number[j+1]:
            number[j] -= 1
            point = j
            for k in range(j+1, len(number)):
                number[k] = 9
            break

    if point != 0:
        for j in reversed(range(point)):
            if number[j] > number[j+1]:
                number[j+1] = 9
                number[j] -= 1

    while number[0] == 0:
        number = number[1:]

    if len(number) > 1:
        solution = reduce(lambda x, y: str(x)+str(y), number)
    else:
        solution = str(number[0])
    print 'Case #' + str(i+1) + ': ' + solution
