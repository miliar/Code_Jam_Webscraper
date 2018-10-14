from sys import argv


class TidyNumber:
    def __init__(self, number):
        self.tidy_number = number
        self.getBiggestTidy(number)

    def getBiggestTidy(self, number):
        number_string = str(number)
        str_len = len(number_string)
        if (str_len == 1): return True

        for i in range(0, str_len):
            if (number_string[i] > number_string[i+1]):
                self.tidy_number = self.tidy_number - int(number_string[1:]) - 1
                return self.getBiggestTidy(self.tidy_number)
            return number_string[i] <= number_string[i + 1] and self.getBiggestTidy(number_string[1:])
        return False

if __name__ == '__main__':
    number = 1000
    with open('tidyinput.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(1, int(content[0])+1):
        print 'Case #{0}: {1}'.format(i, TidyNumber(int(content[i])).tidy_number)
