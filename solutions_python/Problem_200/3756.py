from sys import argv

class TidyNumbers:
    def __init__(self, filename, output_filename):
        self.input_filename = filename
        self.output_filename = output_filename
        self.test_cases = self.read_file()
        self.write_handler = open(self.output_filename, 'w')

    def read_file(self):
        print "Opening %r to read assembly." % self.input_filename
        file_handler = open(self.input_filename, 'r')
        return file_handler.read().splitlines()

    def calculate_tidy_number(self, number):
        tidy_number = number
        untidy = False
        while tidy_number >= 10 and untidy is False:
            num_split = [int(digit) for digit in str(tidy_number)]
            if sorted(num_split) == num_split:
                untidy = True
            else:
                max_val = num_split[0]
                first_lower_val = num_split[-1]
                for num in num_split[1:]:
                    if num >= max_val:
                        max_val = num
                    else:
                        first_lower_val = num
                        break
                lower_val_index = len(num_split) - num_split[::-1].index(first_lower_val) - 1
                rejoined_number = ''.join(str(n) for n in num_split[lower_val_index:])
                number_to_subtract = int(rejoined_number) + 1
                tidy_number -= number_to_subtract

        return tidy_number

    def find_tidy_numbers(self):
        for index, case in enumerate(self.test_cases[1:], start=1):
            tidy_number = self.calculate_tidy_number(int(case))
            result_str = "Case #%i: %i" % (index, tidy_number)
            print result_str
            self.write_handler.write(result_str + "\n")


script, filename, out_file = argv
TidyNumbers(filename, out_file).find_tidy_numbers()

