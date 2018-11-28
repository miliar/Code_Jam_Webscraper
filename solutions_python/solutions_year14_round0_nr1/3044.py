__author__ = 'basit'

# file = open("mag_in.txt")
file = open("A-small-attempt0.in")


def read_int():
    return int(file.readline())

def read_int_array():
    inputs = file.readline().split()
    return [int(x) for x in inputs]

# initialization input
num_of_cases = read_int()

file_output = open("A-small-attempt0.out", "w")

for case in xrange(num_of_cases):
    answer1 = read_int()
    arrangement1 = [ read_int_array() for x in xrange(4) ]
    possible_answers1 = arrangement1[answer1 - 1]

    answer2 = read_int()
    arrangement2 = [ read_int_array() for x in xrange(4) ]
    possible_answers2 = arrangement2[answer2 - 1]

    answers = list(set(possible_answers1).intersection(possible_answers2))

    answer = ''
    if len(answers) == 0:
        answer = "Volunteer cheated!"
    elif len(answers) == 1:
        answer = str(answers[0])
    else:
        answer = "Bad magician!"

    if case > 0:
        file_output.write("\n")

    file_output.write( "Case #%d: %s"%(case+1, answer) )

file_output.close()
