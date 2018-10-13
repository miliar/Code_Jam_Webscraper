#!/usr/bin/env python

def solve(n, people):
    invited = 0
    already_standing = 0
    for index, value in enumerate(people):
        while index > already_standing:
            invited +=1
            already_standing += 1
        already_standing += int(value)

    return invited


def main():
    n_tests = int(raw_input())
    for i in range(n_tests):
        n, people = raw_input().split()
        print 'Case #'+str(i+1)+':', solve(int(n), people)


if __name__ == '__main__':
    main()


##
# Input
    
# Output
 

# 4
# 4 11111
# 1 09
# 5 110011
# 0 1

    

# Case #1: 0
# Case #2: 1
# Case #3: 2
# Case #4: 0
