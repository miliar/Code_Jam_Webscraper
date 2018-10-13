
    
class Round:
    def __init__(self, first_answer, first_arrangement, second_answer, second_arrangement):
        self.first_answer = first_answer
        self.first_arrangement = first_arrangement
        self.second_answer = second_answer
        self.second_arrangement = second_arrangement

num_of_test_cases = 0
rounds = []

def intersect(a, b):
    return list(set(a) & set(b))

def load_data():
    f = open("A-small-attempt0.in.in")
    num_of_test_cases = int(f.readline())
    first_answer = -1
    first_arrangement = []
    second_answer = -1
    second_arrangement = []
    for line in f.readlines():
        if first_answer == -1:
            first_answer = int(line)
        elif len(first_arrangement) < 16:
            first_arrangement += [int(x)  for x in line.split(' ')]
        elif second_answer == -1:
            second_answer = int(line)
        elif len(second_arrangement) < 16:
            second_arrangement += [int(x)  for x in line.split(' ')]
            if(len(second_arrangement) == 16):
                rounds.append(Round(first_answer, first_arrangement, second_answer, second_arrangement))
                first_answer = -1
                first_arrangement = []
                second_answer = -1
                second_arrangement = []
            
        

load_data()
case_number = 0
for round in rounds:
    case_number += 1
    first_answer_row = round.first_arrangement[round.first_answer * 4 - 4:round.first_answer*4]
    second_answer_row = round.second_arrangement[round.second_answer*4 - 4:round.second_answer*4]
    result = intersect(first_answer_row, second_answer_row)
    output_text = 'Case #' + str(case_number) + ': '
    if len(result) == 0:
        print output_text + 'Volunteer cheated!'
    elif len(result) == 1:
        print output_text + str(result[0])
    elif len (result) > 1:
        print output_text + 'Bad magician!'

