""" tidy.py """
import os


class TargetNumber(object):
    """ TargetNumber class """

    def __init__(self, arg):
        self.__current = int(arg.strip())

    def get_result(self):
        """ calculate and return result """
        while True:
            if self.__is_tidy():
                return self.__current
            else:
                self.__current = self.__current - 1

    def __is_tidy(self):
        num_list = list(str(self.__current))
        if len(num_list) == 1:
            return True
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                return False
        return True


def main():
    """ main """

    def __get_results(input_file_name):
        ret = []
        with open(input_file_name) as input_file:
            for line_number, each_line in enumerate(input_file):
                if line_number == 0:  # skip first line
                    continue
                result = TargetNumber(each_line).get_result()
                ret.append('Case #' + str(line_number) + ': ' + str(result))
        return ret

    def __print_result(results):
        for result in results:
            print(result)

    def __out_result(results, output_file_name):
        with open(output_file_name, 'w') as output_file:
            for result in results:
                output_file.write(result + '\n')

    input_file_name = 'B-small-attempt0.in'
    results = __get_results(input_file_name)
    __print_result(results)

    out_result = True
    if out_result:
        output_file_name = os.path.splitext(input_file_name)[0] + '.out'
        __out_result(results, output_file_name)


if __name__ == '__main__':
    main()
