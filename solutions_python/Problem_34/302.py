import sys

# Alg: Have the dictionary as a set. Also add 1, 2, ... L-1 lengths of words
# so that when we do the search, we can search on the first n characters,
# and potentially skip a heap of tests.
#
# I just realised there is a simpler way of doing this. Use regular
# expressions. Change the ( to [ and ) to ] and run every "word" on every
# entry in the dictionary. That is a LOT of tests. So although 8 minutes
# should be enough (I think), I'll keep going with my way for the moment.


def test_word(pattern, dict, num_char, curr_word):
    matches = 0
    for ii in range(len(pattern[num_char])):
        next_word = ''.join([curr_word, pattern[num_char][ii]])
        if next_word in dict:
            if num_char == len(pattern)-1:
                matches += 1
            else:
                matches += test_word(pattern, dict, num_char+1, next_word)

    return matches


#######################
# Main code
#######################
input = sys.stdin.readline().split()
word_length = int(input[0])
dict_length = int(input[1])
num_tests = int(input[2])

# read in the dictionary
dict = set()
for ii in range(dict_length):
    word = sys.stdin.readline()
    for jj in range(1, word_length+1):
        dict.add(word[:jj])

# Now do each test case
for ii in range(num_tests):
    # read the expression
    line = sys.stdin.readline().rstrip()
    pattern = []
    curr_char = ""
    in_brackets = False
    for jj, char in enumerate(line):
        if char != "(" and char != ")":
            # add the char to the curr_char
            if in_brackets:
                curr_char = ''.join([curr_char, char])
            else:
                pattern.append(char)
        elif char == "(":
            in_brackets = True
        elif char == ")":
            pattern.append(curr_char)
            curr_char = ""
            in_brackets = False

    matches = test_word(pattern, dict, 0, "")

    print("Case #" + str(ii+1) + ": " + str(matches))
