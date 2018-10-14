import sys


def is_tidy(number):
    n_str = str(number)
    previous = int(n_str[0])

    for i in range(1, len(n_str)):
        if previous > int(n_str[i]):
            return False
        previous = int(n_str[i])
    return True


print is_tidy(123946)


def countdown(number_as_string):
    last = number_as_string[-1]
    for i in range(0, len(number_as_string)):
        pass


class CountDownIterator:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def next(self):
        if self.number == "0":
            raise StopIteration()
        self.countdown()
        self.remove_leading_zeros()
        return self.number

    def remove_leading_zeros(self):
        if self.number[0] == '0':
            self.number = self.number[1:]
            self.remove_leading_zeros()

    def find_tidy_number(self):
        for i in reversed(range(0, len(self.number) - 1)):
            current = int(self.number[i + 1])
            after = int(self.number[i])
            if after > current:
                after -= 1
                to_append = ''
                for j in range(i + 1, len(self.number)):
                    to_append += '9'
                self.number = self.number[:i + 1] + to_append
                self.number = self.number[:i] + str(after) + self.number[i + 1:]

        self.remove_leading_zeros()
        return self.number

    def countdown(self):
        self.number = self._countdown(self.number)
        return self.number

    def _set(self, string, char, position):
        if position + 1 == len(string):
            return string[:position - 1] + char

        return string[:position - 1] + char + string[position + 1:]


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()[1:]

    with open('output-large.txt', 'w+') as w:
        case = 1
        for line in lines:
            a = CountDownIterator(line.strip())
            w.write("Case #{0}: {1}\n".format(case, a.find_tidy_number()))
            case += 1
        w.close()
