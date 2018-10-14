tests = int(input())
numbers = []

for test in range(1, tests + 1):
    last = int(input())
    result = lambda r: "Case #{}: {}".format(test, r)
    numbers = range(1, last+1)

    for number in numbers[::-1]:
        number_splits = [i for i in str(number)]

        if sorted(number_splits) == number_splits:
            print(result(number))
            break
