""" pancake.py """
import os


class PanCakeRow(object):
    """ PanCakeRow """

    __HAPPY_SIDE = True
    __BLANK_SIDE = False

    def __init__(self, arg1, arg2):
        self.__pancakes = []
        for pancake_str in list(arg1):
            pancake = self.__HAPPY_SIDE if pancake_str == '+' else self.__BLANK_SIDE
            self.__pancakes.append(pancake)
        self.__flipper_size = int(arg2)
        self.__flip_times = 0

    def get_result(self):
        """ calculate and return result """
        while True:
            if self.__are_all_happy_side_up():
                return self.__flip_times
            elif self.__can_do_next_flip():
                self.__do_next_flip()
            else:
                return "IMPOSSIBLE"

    def __are_all_happy_side_up(self):
        if self.__pancakes.count(self.__BLANK_SIDE):
            return False
        return True

    def __can_do_next_flip(self):
        blank_cake_posision = self.__get_leftmost_blank_position()
        if blank_cake_posision + self.__flipper_size <= len(self.__pancakes):
            return True
        return False

    def __do_next_flip(self):
        blank_cake_posision = self.__get_leftmost_blank_position()
        for i in range(self.__flipper_size):
            position = blank_cake_posision + i
            before = self.__pancakes[position]
            after = self.__flip(before)
            self.__pancakes[position] = after
        self.__flip_times = self.__flip_times + 1

    @classmethod
    def __flip(cls, pancake):
        if pancake == cls.__HAPPY_SIDE:
            return cls.__BLANK_SIDE
        else:
            return cls.__HAPPY_SIDE

    def __get_leftmost_blank_position(self):
        position = 0
        for pancake in self.__pancakes:
            if pancake == self.__BLANK_SIDE:
                return position
            position = position + 1
        return -1


def main():
    """ main """

    def __get_results(input_file_name):
        ret = []
        with open(input_file_name) as input_file:
            line_number = 0
            for each_line in input_file:
                if line_number == 0:  # skip first line
                    line_number = line_number + 1
                    continue
                val1, val2 = each_line.strip().split(' ')
                result = PanCakeRow(val1, val2).get_result()
                ret.append('Case #' + str(line_number) + ': ' + str(result))
                line_number = line_number + 1
        return ret

    def __print_result(results):
        for result in results:
            print(result)

    def __out_result(results, output_file_name):
        with open(output_file_name, 'w') as output_file:
            for result in results:
                output_file.write(result + '\n')

    input_file_name = 'A-large.in'
    results = __get_results(input_file_name)
    __print_result(results)

    out_result = True
    if out_result:
        output_file_name = os.path.splitext(input_file_name)[0] + '.out'
        __out_result(results, output_file_name)


if __name__ == '__main__':
    main()
