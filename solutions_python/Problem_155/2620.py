# GCJ 2015 Qualification Round Problem A
# Standing Ovation

##Problem Statement

# It's opening night at the opera, and your friend is the prima donna (the
# lead female singer). You will not be in the audience, but you want to
# make sure she receives a standing ovation -- with every audience
# member standing up and clapping their hands for her.

# Initially, the entire audience is seated. Everyone in the audience has
# a shyness level. An audience member with shyness level Si will wait
# until at least Si other audience members have already stood up to
# clap, and if so, she will immediately stand up and clap. If Si = 0,
# then the audience member will always stand up and clap immediately,
# regardless of what anyone else does. For example, an audience member
# with Si = 2 will be seated at the beginning, but will stand up to clap
# later after she sees at least two other people standing and clapping.

# You know the shyness level of everyone in the audience, and you are
# prepared to invite additional friends of the prima donna to be in the
# audience to ensure that everyone in the crowd stands up and claps in
# the end. Each of these friends may have any shyness value that you
# wish, not necessarily the same. What is the minimum number of friends
# that you need to invite to guarantee a standing ovation?

##Input

# The first line of the input gives the number of test cases, T. T test
# cases follow. Each consists of one line with S_max, the maximum shyness
# level of the shyest person in the audience, followed by a string of
# S_max + 1 single digits. The kth digit of this string (counting
# starting from 0) represents how many people in the audience have
# shyness level k.

#(ex)
# 2 409
# four audience members with S_i = 0, and nine audience members with
# S_i = 2 (and none with S_i = 1 or any other value). Note that there
# will initially always be between 0 and 9 people with each shyness level.

# The string will never end in a 0. Note that this implies that there will
# always be at least one person in the audience.

##Output

# For each test case, output one line containing "Case #x: y", where x
# is the test case number (starting from 1) and y is the minimum number
# of friends you must invite.

##Limits
# 1 <= T <= 100
# 0 <= S_max <= 6 (small dataset)
# 0 <= S_max <= 1000 (large dataset)

import doctest

INFILE = "QR_A_large.in"
OUTFILE = "QR_A_large.out"

def load_file(foo):
    '''
    String -> ListOfInt
    Open a newline and space-delimited text file and do
    the following manipulations:
    (1) Remove all '\n' chars and insert each line into a list
    (2) Split strings into sublists at the ' ' (space) char
    (3) starting from the 2nd element of the list, convert the
        2nd sublist element from string to list
        i.e. ['4', '11111'] -> ['4', ['1','1','1','1','1']]
    '''
    inputL = []
    with open(foo, 'r') as f:
        for line in f:
            line.replace('\n', '')
            inputL.append(line)
            # split S_max + array into sublists containing
            # ['S_max', 'string']; split on SPACE
            inputL[-1] = inputL[-1].split()
        for i in range(1, len(inputL)):
            inputL[i][1] = list(inputL[i][1])
    return inputL

def stringToInt(loS):
    '''
    ListOfString -> ListOfInt
    listof ListOfString -> listof ListOfInt

    >>> stringToInt(['4'])
    [4]
    >>> stringToInt(['4', ['1','1','1']])
    [4, [1, 1, 1]]
    '''
    loi = []
    loi2 = []

    if len(loS) == 1:
        loS[0] = int(loS[0])
        return loS
    elif len(loS) == 2:
        loi.append(int(loS[0]))
        for i in range(len(loS[1])):
            loi2.append(int(loS[1][i]))
        loi.append(loi2)
        return loi


def minInvites(lolos):
    '''
    lolistOfString -> Int
    Given a list of LOS sublists, return an integer >=0
    denoting how many add'l people must be invited to ensure
    a standing ovation for the primadonna

    >>> minInvites(['4', ['1','1','1','1', '1']])
    0
    >>> minInvites(['1', ['0','9']])
    1
    >>> minInvites(['5', ['1','1','0','0','1','1']])
    2
    >>> minInvites(['0', ['1']])
    0
    >>> minInvites(['6', ['1','0','1','0','1','0','1']])
    3
    '''
    # convert lolos (str) to loloi (int)
    loloi = stringToInt(lolos)
    # number of people who will definitely stand
    numStand = loloi[1][0] #initialized with S_0
    # tot no. of add'l people invited to ensure standing ovation
    totalInvite = 0
    S_max = loloi[0]
    audienceList = loloi[1]

    if S_max == 0:
        return 0
    else:
        for i in range(1, S_max + 1):
            numInvite = 0
            if numStand >= i:
                numStand += audienceList[i]
            else:
                numInvite = i - numStand
                numStand += numInvite + audienceList[i]
                totalInvite += numInvite
        return totalInvite

def num_cases(list_file):
    '''
    ListOfString -> Int

    **NOTE**: this function mutates the input list!

    >>> num_cases([['5'], ['1', '2']])
    5
    '''
    ncases = stringToInt(list_file.pop(0))
    return ncases[0]


def next_case(list_file):
    '''
    listof ListOfString -> listofListOfInt
    Given a list of sublists of strings, return the
    next case where a case is defined as a list of the form
    ['a', ['b',...'n']]

    **NOTE**: this function mutates the input list!

    >>> next_case([['4', ['1','1','1']], ['0', ['1']]])
    [4, [1, 1, 1]]
    '''
    nextc = stringToInt(list_file.pop(0))
    return nextc


def write_out(outfile):
    '''
    -> File
    Calls helper functions and writes output to outfile
    '''

    with open(outfile, 'w') as output_file:
        input_list = load_file(INFILE)
        copy_input = input_list
        ans = 0
        case_cnt = 1

        for i in range(num_cases(copy_input)):
            ans = minInvites(next_case(copy_input))
            output_file.write(
                'Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
            case_cnt += 1


## MAIN PROGRAM ##
doctest.testmod()
write_out(OUTFILE)

