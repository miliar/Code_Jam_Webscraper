#!/usr/local/bin/pypy
"Solve 2012-B"
from sys import argv, stdout

def main():
    "entry point"

    myinput = open(argv[1])
    myinput.next()
    linecount = 0
    for line in myinput:
        line = tuple(int(i) for i in line.split())
        suprises = line[1]
        target = line[2]
        scores = line[3:]

        linecount += 1
        stdout.write(
                'Case #%i: %s\n' % (
                    linecount, 
                    solve(target, suprises, scores),
                )
        )

def solve(target, suprises, scores):
    "do the solving"
    found = 0
    for score in scores:
        if max(regular(score)) >= target:
            found += 1
        elif suprises and max(suprise(score)) >= target:
            found += 1
            suprises -= 1
    return found

def regular(total):
    "show the regular judges"
    average, leftover = divmod(total, 3)
    judges = tuple(
            average for i in range(3 - leftover)
    ) + tuple(
            average + 1 for i in range(leftover)
    )
    return judges

def suprise(total):
    "show the suprise judges"
    average, leftover = divmod(total, 3)
    if leftover:
        if average + leftover <= 10:
            judges = (average, average, average + leftover)
        else:
            return regular(total)
    elif average in (0, 10):
        # Can't go out of bounds
        judges = (average, average, average)
    elif average > 0:
        judges = (average - 1, average, average + 1)
    return judges

if __name__ == '__main__':
    main()
