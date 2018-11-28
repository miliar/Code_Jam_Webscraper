import os
from sys import argv
from sys import exit

class Pancake(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = int(params_array[0])
        self.trials = params_array[1:]
        self.answer = []
        self.og_pancakes = False

    def run(self):
        attempt = 1
        for trial in self.trials:
            answer = self.get_answer(trial)
            self.append_answer(answer, attempt)
            attempt += 1


    def get_answer(self, untidy_number, attempt=0):
        print untidy_number
        untidy_int = int(untidy_number)
        if self.is_tidy_number(untidy_int):
            return untidy_number
        return self.get_answer(untidy_int-1)

    def is_tidy_number(self, number):
        number_str = str(number)
        return all(number_str[i] <= number_str[i+1] for i in xrange(len(number_str)-1))


    def append_answer(self, answer, attempt):
        self.answer.append('Case #{0}: {1}'.format(attempt, answer))

    def get_result(self):
        return '\n'.join(self.answer)

def main(file_name):
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    pancake = Pancake(google_input)
    pancake.run()
    answer = pancake.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)


if __name__ == '__main__':
    file_name = argv[1]
    main(file_name)


