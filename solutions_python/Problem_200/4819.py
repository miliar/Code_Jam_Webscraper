def read_file():
    input_file = open("B-small-attempt0.in")
    x = input_file.readline()
    y = input_file.read()
    d = y.split("\n")
    num_tests = int(x)
    test_cases = list()
    '''
    for i in d:
        if i is not "":
            test_cases.append(int(i))
    '''
    test_cases = d
    test_cases.pop(len(test_cases) - 1)

    print("Number of tests: %d" % num_tests)
    print(test_cases)
    input_file.close()
    return num_tests, test_cases


def is_tidy(string_number):
    if len(string_number) == 1:
        return True
    digits = list()
    for dig in string_number:
        digits.append(int(dig))
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    return True


# start code here:

num_tests, test_cases = read_file()
output_file = open("output.txt", "w")

for test_number in range(num_tests):
    test = test_cases[test_number]
    if is_tidy(test):
        print("Case #%d: %s" % (test_number + 1, test))
        output_file.write("Case #%d: %s\n" % (test_number + 1, test))
    else:
        while not is_tidy(test):
            x = int(test) - 1;
            test = str(x)
        print("Case #%d: %s" % (test_number + 1, test))
        output_file.write("Case #%d: %s\n" % (test_number + 1, test))

output_file.close()
