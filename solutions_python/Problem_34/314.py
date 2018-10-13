# Qual 2009 A

import sys

STATE_IN_LETTER_GROUP = 1
STATE_OUTSIDE_LETTER_GROUP = 2


class Case(object):
    
    def __init__(self, case_no):
        self.case_no = case_no
        self.pattern = ''
        self.pattern_sections = None
        self.num_matches = None

    def set_pattern(self, pattern):
        self.pattern = pattern
        self.pattern_sections = []
        state = STATE_OUTSIDE_LETTER_GROUP
        for letter in pattern:
            if letter == '(':
                state = STATE_IN_LETTER_GROUP
                letter_group = ''
            elif letter == ')':
                self.pattern_sections.append(letter_group)
                state = STATE_OUTSIDE_LETTER_GROUP
            else:
                if state == STATE_IN_LETTER_GROUP:
                    letter_group += letter
                else:
                    self.pattern_sections.append(letter)

    def output(self):
        return 'Case #%s: %s' % (self.case_no, self.num_matches)

    def __repr__(self):
        return '<Case %s %s %s %s>' % (self.case_no, self.pattern, 
                                    self.pattern_sections, self.num_matches)



words = []

def process_input(file_name):
    all_cases = []
    f = file(file_name)
    L,D, N = [int(i) for i in f.readline().split(' ')]
    print L, D, N
    for ix in range(D):
        word = f.readline()
        if word[-1] == '\n':
            word = word[:-1]
        words.append(word)
    print words
    for ix in range(N):
        case = Case(ix + 1)
        pattern = f.readline()
        if pattern[-1] == '\n':
            pattern = pattern[:-1]
        case.set_pattern(pattern)
        all_cases.append(case)
    return all_cases


def get_num_matches(case):
    num_matches = 0
    for word in words:
        if matches(case.pattern_sections, word):
            num_matches += 1
    case.num_matches = num_matches
    

def matches(sections, word):
    if len(sections) != len(word):
        return False
    for ix in range(len(word)):
        if not word[ix] in sections[ix]:
            return False
    return True



if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    all_cases = process_input(input_file_name)
    print all_cases

    for case in all_cases:
        get_num_matches(case)

    output_file = file(output_file_name, 'w')
    for case in all_cases:
        print case.output()
        output_file.write(case.output() + '\n')
    output_file.close()
