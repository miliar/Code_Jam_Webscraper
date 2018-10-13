##############################################################
#   ArkadioG @ Google CodeJam 2013
#
#   This is solution for problem Fair & Square
#   Solution using pypy 1.9
#
##############################################################

from math import sqrt

def is_palindrome(s):
    '''(str) -> bool
    Returns True if and only if given string is palindrome.
    Precondition: string is single word (can contain any char ex. space).

    >>> is_palindrome('kayak')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('101')
    True
    '''
    # s[i] and s[j] are the next pair of characters to compare.
    i = 0
    j = len(s) - 1

    # The characters in s[:i] have been successfully compared to those in s[j:].
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i.
    return j <= i

# opening input file
print "Opening input file..."
inpath = "c-small.bin"
inFile = open(inpath, 'r')

# ask for data - number of test cases
#~ N = int(raw_input("Number of test cases: "))
N = int(inFile.readline().rstrip() )
print N, "lines of text in file"
cases = [] # list of testcases

# add N testcases to list
print "Adding lines to list"
for i in range(N):
    #~ testCase = inFile.readline().rstrip()
    cases.append(inFile.readline().rstrip().split(' '))
inFile.close()

#~ print cases

### Let's now compute

# list holding values of Fair&Square values for each testcase
num_of_Fairs = []

# iterate over list containing begining and end values of calculations
for dataset in cases:

    # counter for Fairs&Squares
    counter = 0

    # check values between and icluding boundaries
    for n in xrange(int(dataset[0]), int(dataset[-1]) + 1 ):

        # check if n is palindrome
        if is_palindrome(str(n)):

            # compute square root of n
            root = int(sqrt(n))

            # check if root is perfect sqrt, if is -> if is palindrome
            if root ** 2 == n and is_palindrome(str(root)):

                # increase counter
                counter += 1

    # add value of counter to list holding answers to testcases
    num_of_Fairs.append(counter)

#~ print num_of_Fairs



###########
# open / create file to print in it results
outpath = "c-small.out"
outFile = open(outpath, 'w')
print "Creating output file:", outpath

# printout cases to file - one at each line
case = 1                        # number of case
# move along every element of reversed list and print it in lines
print "Writing data into file..."
for i in num_of_Fairs:
    line = "Case #" + str(case) + ":" + " " + str(i) + "\n"  #add \n to start next line
    outFile.write(line)
    case += 1
outFile.close()
print "Finished"                    # all ok
