# GCJ 2014 Qualification Round Problem A
# Magic Trick

# Recently you went to a magic show. You were very impressed by one of
# the tricks, so you decided to try to figure out the secret behind
# it!

#The magician starts by arranging 16 cards in a square grid: 4 rows of
#cards, with 4 cards in each row. Each card has a different number
#from 1 to 16 written on the side that is showing. Next, the magician
#asks a volunteer to choose a card, and to tell him which row that
#card is in.

#Finally, the magician arranges the 16 cards in a square grid again,
#possibly in a different order. Once again, he asks the volunteer
#which row her card is in. With only the answers to these two
#questions, the magician then correctly determines which card the
#volunteer chose. Amazing, right?

#You decide to write a program to help you understand the magician's
#technique. The program will be given the two arrangements of the
#cards, and the volunteer's answers to the two questions: the row
#number of the selected card in the first arrangement, and the row
#number of the selected card in the second arrangement. The rows are
#numbered 1 to 4 from top to bottom.

#Your program should determine which card the volunteer chose; or if
#there is more than one card the volunteer might have chosen (the
#magician did a bad job); or if there's no card consistent with the
#volunteer's answers (the volunteer cheated).

#Input

#The first line of the input gives the number of test cases, T. T test
#cases follow. Each test case starts with a line containing an
#integer: the answer to the first question. The next 4 lines represent
#the first arrangement of the cards: each contains 4 integers,
#separated by a single space. The next line contains the answer to the
#second question, and the following four lines contain the second
#arrangement in the same format.

#Output

#For each test case, output one line containing "Case #x: y", where x
#is the test case number (starting from 1).

#If there is a single card the volunteer could have chosen, y should
#be the number on the card. If there are multiple cards the volunteer
#could have chosen, y should be "Bad magician!", without the
#quotes. If there are no cards consistent with the volunteer's
#answers, y should be "Volunteer cheated!", without the quotes. The
#text needs to be exactly right, so consider copying/pasting it from
#here.

#Limits

#1 <= T <= 100.
#1 <= both answers <= 4. (row numbers containing the user's choice)
#Each number from 1 to 16 will appear exactly once in each arrangement.

FILE_NAME = "QR_A-MagicTrick_small-attempt0.in"
OUTPUT = "QR_A-MagicTrick_small-attempt0.out"

def load_file():
    '''open text file and insert each line into a list'''
    in_file = open(FILE_NAME, 'r', 0)
    line_list = list(in_file)
    in_file.close()
    # remove all newline chars from the list of strings
    line_list = [i.strip('\n') for i in line_list]
    # convert strings to lists to make list of lists
    line_list = [line_list[i].split() for i in range(len(line_list))]
    # cast all list elements to type int
    line_list = [map(int, line_list[i]) for i in range(len(line_list))]
    return line_list

def num_cases(list_file):
    '''
    ListOf Natural -> Natural
    Given a list of lines containing Naturals, return a Natural
    denoting the number of cases to consider.
    **NOTE**: this function mutates the input list!

    >>> num_cases([[3], [2], [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    3
    '''
    ncases = list_file.pop(0)[0]
    return ncases

def next_case(list_file):
    '''
    ListOf int -> ListOf int
    Given a list of lines containing sublists of ints, return the
    next case where a case is defined as a line of form
    [a, b, c, d]
    where a ~ d are all ints. To find the appropriate line, we need
    to reference the row number, which is the first element of the
    first sublist

    **NOTE**: this function mutates the input list!

    >>> next_case([[2], [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    [5, 6, 7, 8]

    >>> next_case([[3], [1,2,5,4], [3,11,6,15], [9,10,7,12], [13,14,8,16]])
    [9, 10, 7, 12]
    '''
    row_num = list_file[0][0]
    nextc = list_file.pop(row_num)
    del list_file[0:4]
    return nextc

def magic_trick_result(row1, row2):
    '''
    ListOfInt ListOfInt -> String
    Given two rows containing four ints each, return one of three
    answers:
    int (only 1 int in common element from row1, row2)
    Bad magician! (2 or more ints are in common from row1, row2)
    Volunteer cheated! (no ints in common from row1, row2)

    >>> magic_trick_result([5,6,7,8], [9,10,7,12])
    7

    >>> magic_trick_result([5,6,7,8], [5,6,7,8])
    'Bad magician!'

    >>> magic_trick_result([5,6,7,8], [9,10,11,12])
    'Volunteer cheated!'
    '''
    set1 = set(row1)
    set2 = set(row2)
    intersect12 = list(set1 & set2)

    if len(intersect12) == 0:
        return "Volunteer cheated!"
    elif len(intersect12) == 1:
        return intersect12[0]
    else:
        return "Bad magician!"

def write_out(outfile):
    '''
    -> File
    Calls helper functions and writes output to outfile
    '''

    output_file = open(outfile, 'w')
    input_list = load_file()
    copy_input = input_list
    ans = 0
    case_cnt = 1

    for i in range(num_cases(copy_input)):
        row1 = next_case(copy_input)
        row2 = next_case(copy_input)
        ans = magic_trick_result(row1, row2)
        output_file.write(
            'Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
        case_cnt += 1
    output_file.close()

## MAIN PROGRAM ##
write_out(OUTPUT)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
