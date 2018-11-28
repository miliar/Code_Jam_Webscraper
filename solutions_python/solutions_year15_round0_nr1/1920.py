__author__ = 'nati'


INPUT_FILE = "/home/nati/Downloads/A-large.in"
OUTPUT_FILE = "/home/nati/Downloads/A-large.out"


def so():
    with open(INPUT_FILE) as file_input, open(OUTPUT_FILE, 'w') as file_output:
        test_cases = int(file_input.readline().strip())
        for case in xrange(test_cases):
            smax, crowd = file_input.readline().strip().split()
            crowd = [int(c) for c in crowd]
            guests = 0
            for i in xrange(1, len(crowd)):
                if i:
                    guests += max(i - sum(crowd[:i]) - guests, 0)
            file_output.write("case #{case}: {guests}\n".format(case=case+1,
                                                                guests=guests))


if __name__ == "__main__":
    so()