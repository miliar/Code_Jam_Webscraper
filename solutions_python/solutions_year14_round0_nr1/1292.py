#!/usr/local/bin/python
import argparse
from itertools import islice

def main():
    # Take input
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()

    # Read input
    cases = []
    with open(args.input) as f:
        n = int(f.readline())
        for i in range(n):
            cases.append("".join(list(islice(f, 10))))

    # Handle cases
    handleCases(cases)

def handleCases(cases):
    for i, case in enumerate(cases):
        print "Case #{n}: {result}".format(n=i+1, result=handleCase(case))

def handleCase(case):
    # Separate rounds
    arr = filter(None, case.split("\n"))
    r1 = arr[:len(arr)/2]
    r2 = arr[len(arr)/2:]

    s1 = [int(x) for x in r1[int(r1[0])].split(" ")]
    s2 = [int(y) for y in r2[int(r2[0])].split(" ")]

    union = set(s1).intersection(s2)

    if len(union) == 1:
        (result,) = union
        return result
    elif len(union) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


if __name__ == "__main__":
    main()
