import sys

#returns a list with the strings in separated groups like
#(zyx)bc -> ['zyx', 'b', 'c']
def parse_test_case(test_case):
    if not '(' in test_case:
        return list(test_case)

    splited = [s.split(')') for s in test_case.split('(') if s]

    parts = []
    for i in range(len(splited)):
        for j in range(len(splited[i])):
            if j == 0:
                parts.append(splited[i][j])
            else:
                chars = list(splited[i][j])
                for char in chars:
                    parts.append(char)

    return parts

#print parse_test_case("(zyx)bc")
#assert parse_test_case("(zyx)bc") == ['zyx', 'b', 'c']
#
#print parse_test_case("(ab)(bc)(ca)")
#assert parse_test_case("(ab)(bc)(ca)") == ['ab', 'bc', 'ca']
#
#print parse_test_case("abc")
#assert parse_test_case("abc") == ['a', 'b', 'c']
#
#print parse_test_case("(abc)(abc)(abc)")
#assert parse_test_case("(abc)(abc)(abc)") == ['abc', 'abc', 'abc']

def how_many_match(words, test_case):
    parts = parse_test_case(test_case)

    n_match = 0
    for word in words:
        char_match = 0

        for j in range(len(parts)):
            if not word[j] in parts[j]:
                break
            elif j == len(parts) - 1:
                n_match += 1

    return n_match


(length, n_words, n_test_cases) = sys.stdin.readline().split(' ')

length = int(length)
n_words = int(n_words)
n_test_cases = int(n_test_cases)

words = []
for i in range(n_words):
    words.append(sys.stdin.readline().strip())

test_cases = []
for i in range(n_test_cases):
    test_cases.append(sys.stdin.readline().strip())


for i in range(len(test_cases)):
    n_match = how_many_match(words, test_cases[i])
    print "Case #%d: %d" % (i + 1, n_match)

