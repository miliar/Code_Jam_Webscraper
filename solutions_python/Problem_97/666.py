import sys

in_file = open(sys.argv[1])

num_test_cases = int(in_file.readline().strip())

for i in range(num_test_cases):
    entry = in_file.readline().strip().split(' ')
    entry = [int(x) for x in entry]
    A = entry[0]
    B = entry[1]
    answers = set()
    for number in range(A, B+1):
        str_number = repr(number)
        for j in range(1, len(str_number)):
            new_number = int(str_number[j:] + str_number[:j])
            if number < new_number <= B:
                answers.add((number,new_number))

    print "Case #%s: %s" % (i+1, len(answers))


