# Created by PyCharm.
# User: tomhydra
# Date: 4/8/17

class Main:
    def __init__(self, input_file_name):
        self.output_file_name = "output.txt"
        self.input_file = open(input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        test_cases = eval(self.input_file.readline())
        for i in range(test_cases):
            lst = [int(x) for x in self.input_file.readline().split()]
            stalls = lst[0]
            persons = lst[1]
            num_max, num_min = self.calculator(stalls, persons)
            self.output_file.write("Case #{0}: {1} {2}\n".format(i + 1, num_max, num_min))
            # print("Case #{0}: {1} {2}\n".format(i + 1, num_max, num_min))

    def calculator(self, stalls, persons):
        num_max = num_min = 0
        duplicate = 0
        stalls_list = {stalls:1}

        if stalls == persons:
            return num_max, num_min
        i = 0
        while i < persons:
            current = max(stalls_list.keys())
            if current == 1:
                return 0, 0
            num = current // 2
            num_max = num
            num_min = num - 1 if current % 2 == 0 else num
            # self.output_file.write("First {0} {1}\n".format(stalls_list, i))

            if stalls_list[current] == 1 and duplicate == 0:
                # self.output_file.write("_\n")
                stalls_list.pop(current)
                stalls_list[num_max] = stalls_list[num_max] + 1 \
                    if num_max in stalls_list else \
                    1
                stalls_list[num_min] = stalls_list[num_min] + 1 \
                    if num_min in stalls_list else \
                    1
            elif duplicate == 0:
                value_to_add = stalls_list[current]
                stalls_list[num_max] = stalls_list[num_max] + value_to_add \
                    if num_max in stalls_list else \
                    value_to_add
                stalls_list[num_min] = stalls_list[num_min] + value_to_add \
                    if num_min in stalls_list else \
                    value_to_add
                duplicate = stalls_list[current]
                stalls_list[current] = 1
                stalls_list.pop(current)


            # self.output_file.write("{0} {1}\n".format(stalls_list, i))
            i += duplicate + 0 if duplicate > 0 else 1
            duplicate = 0


        return num_max, num_min




Main("A-small-practice.in")
#Main("A-large-practice.in")