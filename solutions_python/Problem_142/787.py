"""
Jonathan Simowitz

Google Code Jam 2014
Round 1B
"""

import os


def base_form(string):
    previous_char = None
    count = 0
    form = []
    for idx, char in enumerate(string):
        if idx == 0:
            count = 1
            previous_char = char
        elif char == previous_char:
            count += 1
        elif char != previous_char:
            form.append((previous_char, count))
            previous_char = char
            count = 1
        if idx == len(string) - 1:
            form.append((char, count))
    return form


def calc_moves(dupes):
    ave = sum(dupes) / len(dupes)
    moves = 0
    for dupe in dupes:
        if dupe == ave:
            continue
        else:
            moves += abs(ave - dupe)
    return moves


def repeater(strings):
    forms = []
    len_form = None
    for string in strings:
        form = base_form(string)
        if len_form is None:
            len_form = len(form)
        elif len_form != len(form):
            return 'Fegla Won'
        forms.append(form)
    if not forms or not forms[0]:
        return 'Fegla Won'
    try:
        moves = 0
        for i in range(len_form):
            char = None
            counts = []
            for form in forms:
                if char is None:
                    char = form[i][0]
                elif char != form[i][0]:
                    return 'Fegla Won'
                counts.append(form[i][1])
            moves += calc_moves(counts)
    except Exception:
        return 'Fegla Won'
    return moves


def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "A-small-attempt0.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    num_test_cases = int(rf.readline().strip())
    for test_num in range(1, num_test_cases + 1):
        num_strings = int(rf.readline().strip())
        strings = []
        for string in range(num_strings):
            strings.append(rf.readline().strip())
        result = repeater(strings)
        wf.write('Case #%d: %s\n' % (test_num, result))
    rf.close()
    wf.close()


main()
