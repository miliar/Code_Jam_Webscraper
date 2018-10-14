# Created by PyCharm.
# User: tomhydra
# Date: 4/8/17

class Main:
    def __init__(self, input_file_name):
        self.output_file_name = "output.txt"
        self.input_file = open(input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.calculator()

    def calculator(self):
        test_cases = eval(self.input_file.readline())
        for i in range(test_cases):
            read = self.input_file.readline()
            self.N = int(read)
            N_splitted = [int(x) for x in list(str(self.N))]
            self.output_file.write("Case #{0}: {1}\n".format(i + 1, self.getTidy(N_splitted)))
            # print("Case #{0}: {1}\n".format(i + 1, self.getTidy(N_splitted)))

    def getTidy(self, splitted):
        for i in range (len(splitted)):
            if i > 0 and splitted[i] < splitted[i-1]:
                for j in range(i - 1 , 0, -1):
                    if splitted[j] <= splitted[j-1]:
                        splitted[j] = 0
                    else:
                        break
                for k in range(i, len(splitted)):
                    splitted[k] = 0
                self.N = int(''.join(list(map(str, splitted))))
                return self.N - (splitted[i] + 1)
        return self.N

Main("A-small-practice.in")
#Main("A-large-practice.in")