#!/usr/local/bin/pypy
"Solve 2012-B"
from sys import argv, stdout

def main():
    "entry point"

    myinput = open(argv[1])
    myinput.next()
    linecount = 0
    for line in myinput:
        line = line.split()

        digits = len(line[0])
        mini = int(line[0])
        maxi = int(line[1])

        linecount += 1
        stdout.write(
                'Case #%i: %s\n' % (
                    linecount, 
                    solve(digits, mini, maxi),
                )
        )

def solve(digits, mini, maxi):
    "do the solving"
    found = 0
    for i in range(mini, maxi+1):
        found += find(i, maxi, digits)
    return found

def find(i, maxi, digits):
    "find the number of unique recycled pairs between i and maxi"
    found = 0
    roti = i
    j = 1
    #print i
    while j < digits: # No need to rotate all the way around
        roti = rotate(roti, digits)
        if roti == i:
            # If we hit a symmetry, we can stop
            break
        if i < roti <= maxi:
            found += 1
            #print ' found:', i, j, roti
        j += 1
    return found

def rotate(i, digits):
    "rotate a number by one digit. `digits` is the length of the number."
    digits = '%0*i' % (digits, i)
    digits = digits[-1] + digits[:-1]
    return int(digits, 10)

if __name__ == '__main__':
    main()
