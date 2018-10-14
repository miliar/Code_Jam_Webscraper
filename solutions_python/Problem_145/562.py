#!python3
"""Problem A. Part Elf
https://code.google.com/codejam/contest/3004486/dashboard#s=p0

Vida says she's part Elf: that at least one of her ancestors was an Elf. But she doesn't know if it was a parent (1 generation ago), a grandparent (2 generations ago), or someone from even more generations ago. Help her out!

Being part Elf works the way you probably expect. People who are Elves, Humans and part-Elves are all created in the same way: two parents get together and have a baby. If one parent is A/B Elf, and the other parent is C/D Elf, then their baby will be (A/B + C/D) / 2 Elf. For example, if someone who is 0/1 Elf and someone who is 1/2 Elf have a baby, that baby will be 1/4 Elf.

Vida is certain about one thing: 40 generations ago, she had 240 different ancestors, and each one of them was 1/1 Elf or 0/1 Elf.

Vida says she's P/Q Elf. Tell her what is the minimum number of generations ago that there could have been a 1/1 Elf in her family. If it is not possible for her to be P/Q Elf, tell her that she must be wrong!"""

from fractions import Fraction

powers_of_two = [2**n for n in range(1, 40+1)]

def solve(p, q):
    """For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of generations ago a 1/1 Elf in her family could have been if she is P/Q Elf. If it's impossible that Vida could be P/Q Elf, y should be the string "impossible" (without the quotes)."""
    # reduce to lowest terms
    x = Fraction(p, q)
    p, q = x.numerator, x.denominator

    if q not in powers_of_two:
        return "impossible"

    # smallest n such that 2**n <= x
    for n in range(1, 40+1):
        if Fraction(1, 2**n) <= x:
            return n

    return "impossible"


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    """The first line of the input gives the number of test cases, T. T lines follow. Each contains a fraction of the form P/Q, where P and Q are integers."""

    T = int(f.readline())

    for case in range(1, T+1):
        p, q = [int(x) for x in f.readline().split("/")]

        answer = solve(p, q)
        print("Case #{0}: {1}".format(case, answer))
