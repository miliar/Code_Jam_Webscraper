import sys

def get_data(file_name):
    input_file = open(file_name)
    L, D, N = [int(x) for x in input_file.readline().strip().split()]
    words = []
    for index in range(D):
        words.append(input_file.readline().strip())
    cases = []
    for index in range(N):
        cases.append(input_file.readline().strip())
    input_file.close()
    return L, words, cases

def match(word, case_group):
    for index in range(len(word)):
        character = word[index]
        if character in case_group[index]:
            pass
        else:
            return False
    return True

def split(case):
    index = 0
    case_group = []
    
    in_group = False
    for character in case:
        if character == "(":
            in_group = True
            case_group.append("")
        elif character == ")":
            in_group = False
        else:
            if in_group:
                case_group[index]=case_group[index] + character
            else:
                case_group.append(character)
        if in_group == False:
            index = index + 1
    return case_group
          
length, words, cases = get_data(sys.argv[1])

case_number = 1
for case in cases:
    case_group = split(case)
    matches = 0
    for word in words:
        if match(word, case_group):
            matches = matches + 1
    print "Case #" + str(case_number) + ": " + str(matches)
    case_number = case_number + 1