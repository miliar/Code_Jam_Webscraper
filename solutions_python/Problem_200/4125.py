#! /usr/bin/env python3

def can_proceed_with_mag(n, rest):
    for r in rest:
        if r < n:
            return False
    return True

def construct_largest_tidy(num):
    numerals = reversed([int(n) for n in num])
    largest_tidy = []
    lastn_special = False

    for idx, n in enumerate(numerals):
        #print("dealing with %d" % n)
        if not lastn_special and (not largest_tidy or n <= largest_tidy[0]):
            largest_tidy.insert(0, n)
        else:
            if (n - 1) == 0:
                largest_tidy = [9 for _ in range(idx)]
                lastn_special = True
            else:
                #largest_tidy[0] = 9
                largest_tidy = [9 for _ in range(idx)]
                largest_tidy.insert(0, n-1)
                lastn_special = False
        #print("largest tidy so far %s" % largest_tidy)

    return int("".join([str(_) for _ in largest_tidy]))

if __name__ == "__main__":
    casecount = int(input())

    for case in range(casecount):
        num = input()
        print("Case #%d: %d" % (case + 1, construct_largest_tidy(num)))
