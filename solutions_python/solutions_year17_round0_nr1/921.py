# Created by PyCharm.
# User: tomhydra
# Date: 4/8/17

class Main:
    def __init__(self, input_file_name):
        self.output_file_name = "output.txt"
        self.input_file = open(input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.flips = 0
        self.impossible = False
        self.calculator()

    def calculator(self):
        test_cases = eval(self.input_file.readline())
        for i in range(test_cases):
            line = self.input_file.readline().split()
            lst = list(line[0])
            S = [True if x == '+' else False for x in lst]
            K = int(line[1])
            self.flipper(S, K)
            self.output_file.write("Case #{0}: {1}\n".format(i + 1, 'IMPOSSIBLE' if self.impossible else self.flips))
            self.flips = 0
            self.impossible = False

    def flipper(self, pancakes, flip_length):
        count = 0
        blank_side = 0
        for i in range (len(pancakes)):
            count += 1
            if not pancakes[i]:
                blank_side += 1
            if count == flip_length and blank_side > 0:
                for j in range(flip_length):
                    pancakes[i - j] = not pancakes[i - j]
                self.flips += 1
                self.flipper(pancakes, flip_length)
                blank_side = count = 0
            if blank_side == 0:
                count = 0
        for i in range(len(pancakes)):
            if not pancakes[i]:
                self.impossible = True;




Main("A-small-practice.in")
#Main("A-large-practice.in")