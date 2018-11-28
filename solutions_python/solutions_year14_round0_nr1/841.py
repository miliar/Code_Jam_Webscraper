#!/usr/bin/python3

##########
# Sample Input
#Input 

# 3
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 3
# 1 2 5 4
# 3 11 6 15
# 9 10 7 12
# 13 14 8 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 2
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# 3
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

#Output

# Case #1: 7
# Case #2: Bad magician!
# Case #3: Volunteer cheated!

TEST_CASES = { }
TESTS = 0


def identify_number(ans1,arr1,ans2,arr2):
    match_set = set(arr1[ans1 - 1]).intersection(set(arr2[ans2 - 1]))
    if len(match_set) == 1:
        return list(match_set)[0]
    elif len(match_set) == 0:
        return "Volunteer cheated!"
    elif len(match_set) > 1:
        return "Bad magician!"


def give_nextline(filename):
    with open(filename) as in_file:
        for line in in_file:
            if line is not None:
                yield line
            else:
                yield None



def run_tests(filename):
    
    nextline = give_nextline(filename)
    TESTS = int(next(nextline))
            
    for it in range(1,TESTS + 1):
        ans1 = int( next(nextline) )
        arr1 = [ map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')) ]

        ans2 = int( next(nextline) )

        arr2 = [ map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')),
                 map(int,next(nextline).split(' ')) ]

        
        print('Case #' + str(it) + ': ' + str(identify_number(ans1, arr1, ans2, arr2)) )

    return
              
import sys

tests_file = sys.argv[1] if len(sys.argv) > 1 else "input.data"

run_tests(tests_file)
