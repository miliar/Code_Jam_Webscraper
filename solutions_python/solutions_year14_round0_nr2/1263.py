#!/usr/local/bin/python
import argparse

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
            cases.append(f.readline())

    # Handle cases
    handleCases(cases)

def handleCases(cases):
    for i, case in enumerate(cases):
        print "Case #{n}: {result}".format(n=i+1, result=handleCase(case))

def handleCase(case):
    # Set precision and initial rate and time
    rate = 2.0
    time = 0.0
    (c, f, x) = [float(x) for x in case[:-1].split(" ")]
    #print "{c} {f} {x}".format(c=c, f=f, x=x)

    # Buying farms until no longer practical
    while x/rate > (c/rate + x/(rate + f)):
        time += c/rate
        rate += f

    # Obtaining required number of cookies
    # I should have 0 cookies at this point
    time += x/rate

    return '%.7f' % time

if __name__ == "__main__":
    main()
