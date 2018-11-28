# Created by PyCharm.
# User: tomhydra
# Date: 4/22/17
# Time: 7:16 PM

class Main:
    def __init__(self, input_file_name):
        self.output_file_name = "output.txt"
        self.input_file = open(input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.calculator()

    def calculator(self):
        test_cases = eval(self.input_file.readline())
        for i in range(test_cases):
            times = []
            destination, horses = map(int, self.input_file.readline().split())
            for j in range(horses):
                start, rate = map(int, self.input_file.readline().split())
                times.append((destination - start)/rate)
            times.sort()
            self.output_file.write("Case #{0}: {1:6f}\n".format(i + 1, destination / times.pop()))


Main("A-small-practice.in")
#Main("A-large-practice.in")