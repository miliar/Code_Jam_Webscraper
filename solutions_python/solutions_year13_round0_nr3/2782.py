import math

def check_pallindrome(str):
    if str == str[::-1]:
        return True
    return False

def perfect_squares(A, B):
    min = int(math.ceil(math.sqrt(A)))
    max = int(math.sqrt(B))
    return (n ** 2 for n in xrange(min, max + 1))

T = raw_input('')  # number of test cases
allInput = {}

for case in xrange(0, int(T)):  # for each test case
    range = list(raw_input('').split())  # in the format of A B
    allInput[case] = range

for case in allInput:
    count = 0
    A = int(allInput[case][0])
    B = int(allInput[case][1])
    list_sq = perfect_squares(A, B)
    for val in list_sq:
        if check_pallindrome(str(val)) == True and check_pallindrome(str(int(math.sqrt(val)))) == True:
            count += 1 
    print "Case #" + str(case+1) + ": " + str(count)