#!/usr/bin/env python
import sys


# helper
def log(message):
    sys.stderr.write(message + "\n")



def test(n, case):
    log('test case: {}'.format(case))
    first_answer, first_arrangement, second_answer, second_arrangement = case

    first = set((c for c in first_arrangement[first_answer-1]))
    second = set((c for c in second_arrangement[second_answer-1]))
    candidates = first & second

    if len(candidates) == 1:
        y = candidates.pop()
    elif len(candidates) > 1:
        y = "Bad magician!"
    else:
        y = "Volunteer cheated!"

    print "Case #{n}: {answer}".format(n=n, answer=y)


def parse_matrix(rows):
    """given rows represented as strings of ints, return a matrix."""
    matrix = []
    for n, row in enumerate(rows):
        r = map(int, row.split(" "))
        matrix.append(r)
    return matrix

def parse_input(stream):
    test_cases_to_expect = int(stream.readline())
    for n in range(test_cases_to_expect):
        first_answer = int(stream.readline())
        a,b,c,d = stream.readline(), stream.readline(), stream.readline(), stream.readline()
        first_arrangement = parse_matrix([a, b, c, d])
        second_answer = int(stream.readline())
        e,f,g,h = stream.readline(), stream.readline(), stream.readline(), stream.readline()
        second_arrangement = parse_matrix([e, f, g, h])

        test_case = (first_answer, first_arrangement, second_answer, second_arrangement)
        yield test_case

if __name__ == '__main__':
    for n, test_case in enumerate(parse_input(sys.stdin), start=1):
        test(n, test_case)
