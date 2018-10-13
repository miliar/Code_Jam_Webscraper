import sys
import os

case_win = "Case #%s: "
bad_magic = "Bad magician!"
cheated_volounteer = "Volunteer cheated!"

def get_answer(file_in):
    first_line = int(file_in.readline().strip())
    first_set = set()
    for i in xrange(1, 5):
        x = file_in.readline().strip()
        if i == first_line:
            first_set = set(map(int, x.split(" ")))
    second_line = int(file_in.readline().strip())
    second_set = set()
    for i in xrange(1, 5):
        x = file_in.readline().strip()
        if i == second_line:
            second_set = set(map(int, x.split(" ")))

    result = second_set & first_set
    if len(result) == 0:
        return cheated_volounteer
    elif len(result) > 1:
        return bad_magic
    else:
        return result.pop()
    


def make_work(input='input.txt', output='output.txt'):
    file_in = open(input)
    cases_number = int(file_in.readline().strip())
    for n in xrange(1, cases_number + 1):
        answer = get_answer(file_in)
        
        print((case_win % n) + str(answer))


if len(sys.argv) >= 2:
    make_work(input=sys.argv[1])
else:
    make_work()