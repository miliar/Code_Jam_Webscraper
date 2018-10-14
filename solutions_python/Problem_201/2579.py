""" bathroom.py """
import os


class BathroomStalls(object):
    """ BathroomStalls """

    def __init__(self, arg1, arg2):
        """ 'O' stands for an occupied stall and '.' for an empty one """
        self.stalls = ['.'] * int(arg1)
        self.stalls.insert(0, '0')
        self.stalls.append('0')
        self.people = int(arg2)

    def get_result(self):
        """ calculate and return result """
        for i in range(self.people):
            max_value, min_value = self.__put_people_in_stall()
        return max_value, min_value

    def __put_people_in_stall(self):
        chosed_stall_index, max_value, min_value = self.__choose_stall()
        self.stalls[chosed_stall_index] = '0'
        #self.__out()
        return max_value, min_value

    def __choose_stall(self):
        min_list, max_list = self.__get_min_and_max_distance_list()
        max_value_of_min_list = max(min_list)

        candidate_list = [-1] * len(self.stalls)
        for i, each in enumerate(min_list):
            if each == max_value_of_min_list:
                candidate_list[i] = max_list[i]
        max_value_of_candidate_list = max(candidate_list)

        return candidate_list.index(
            max_value_of_candidate_list
        ), max_value_of_candidate_list, max_value_of_min_list

    def __get_min_and_max_distance_list(self):
        min_list = [-1] * len(self.stalls)
        max_list = [-1] * len(self.stalls)
        for i, stall in enumerate(self.stalls):
            if stall == '0':
                continue
            min_list[i], max_list[i] = self.__get_min_and_max_distance(i)
        return min_list, max_list

    def __get_min_and_max_distance(self, index):
        left = self.__get_left_distance(index)
        right = self.__get_right_distance(index)
        return min(left, right), max(left, right)

    def __get_left_distance(self, index):
        for i, stall in enumerate(reversed(self.stalls[:index])):
            if stall == '0':
                return i
        return -1

    def __get_right_distance(self, index):
        for i, stall in enumerate(self.stalls[index + 1:]):
            if stall == '0':
                return i
        return -1

    def __out(self):
        """ for debug """
        for stall in self.stalls:
            print(stall, end='')
        print()


def main():
    """ main """

    def __get_results(input_file_name):
        ret = []
        with open(input_file_name) as input_file:
            for line_number, each_line in enumerate(input_file):
                if line_number == 0:  # skip first line
                    continue
                val1, val2 = each_line.strip().split(' ')
                result1, result2 = BathroomStalls(val1, val2).get_result()
                ret.append(
                    'Case #{0}: {1} {2}'.format(line_number, result1, result2))
        return ret

    def __print_result(results):
        for result in results:
            print(result)

    def __out_result(results, output_file_name):
        with open(output_file_name, 'w') as output_file:
            for result in results:
                output_file.write(result + '\n')

    input_file_name = 'C-small-1-attempt0.in'
    results = __get_results(input_file_name)
    __print_result(results)

    out_result = True
    if out_result:
        output_file_name = os.path.splitext(input_file_name)[0] + '.out'
        __out_result(results, output_file_name)


if __name__ == '__main__':
    main()
