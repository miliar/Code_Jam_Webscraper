import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

class Test(object):
    def __init__(self, end):
        self.end = end
        self.result = "???"

class Input(object):
    def __init__(self):
        self.tests = []

class Output(object):
    def __init__(self):
        self.tests = None

class Parser(object):
    def  __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        file = open(self.file_name, 'r')

        input = Input()
        for line in file.readlines()[1:]:
            if line[0] == "#":
                logging.debug("skip")
                continue
            end = int(line)
            logging.debug("in:" + str(end))
            input.tests.append(Test(end))

        file.close()
        return input

    def write(self, output):
        self.file = open('out_' + self.file_name, 'w')
        self.write_object(output)
        self.file.close()

    def write_object(self, output):
        for i in range(1, len(output.tests) +1):
            self.write_test(i, output.tests[i-1])
        logging.debug("result: " + str(len(output.tests)) + " tests")

    def write_test(self, i, test):
        self.write_line("Case #" + str(i) + ": " + test.result)

    def write_line(self, line):
        self.file.write(line + "\n")

class Executor(object):
    def __init__(self):
        pass

    def method(self, input):
        output = Output()
        output.tests = input.tests

        for test in output.tests:
            self.execute_test(test)
        return output

    def execute_test(self, test):
        x = test.end
        logging.debug("Until:" + str(x))

        while x > 0:
            if self.is_tidy(x):
                test.result = str(x)
                break
            x = self.find_next(x)
        else:
            test.result = "ERROR"

    def is_tidy(self, x):
        string = str(x)
        for n in range(1, len(string)):
            a = int(string[n-1])
            b = int(string[n])
            if b < a:
                return False
        return True

    def find_next(self, _x):
        x = str(_x)
        y = ""

        error = False
        for n in range(1, len(x)):
            a = int(x[n - 1])
            b = int(x[n])
            if error:
                y += "9"
            elif b < a:
                error = True
                y += str(a-1)
            else:
                y += str(a)

        if error:
            y += "9"
        else:
            y += x[-1]

        logging.debug(x + " => " + y)
        return int(y)

def main():
    parser = Parser("tidy_numbers_3_large.txt")

    out = Executor().method(parser.parse())
    parser.write(out)

if __name__ == "__main__":
    main()


