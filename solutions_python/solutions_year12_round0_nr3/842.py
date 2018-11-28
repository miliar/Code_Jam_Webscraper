#! /usr/bin/env python3 -O

##########
## Adam Sorkin
## Google codejam qual c
## Apr 13, 2012
##########

def main():
    "Compute number of recycled numbers (cyclic perms of each other)"

    T = int(input()) # test cases
    for i in range(1, T+1):
        raw_bounds = input().split()
        A = int(raw_bounds[0]); B = int(raw_bounds[1])
        numbers = [ j for j in range(A, B+1) ]
        answer = 0
        while numbers != []:
            perms = permute(numbers[0])
            good_perms = []
            for num in perms:
                if num <= B and num >=A:
                    numbers.remove(num)
                    good_perms.append(num)
            answer += len(good_perms) * (len(good_perms) - 1) / 2
        print("Case #{0}: {1}".format(i, int(answer)) )
    return

def permute(n):
    "returns the list of distinct numbers obtainable from cyclic perms of n."

    pattern = str(n)
    perms = {n}
    for _ in range(len(pattern)-1):
        pattern = pattern[-1] + pattern[:-1]
        perms.add( int(pattern) )
    return list(perms)




if __name__ == "__main__":
    main()
