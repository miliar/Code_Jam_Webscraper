import logging

logging.basicConfig(level=logging.DEBUG)

class Test(object):
    def __init__(self, string, k):
        self.string = string
        self.k = k
        self.result = "XXX"

class Input(object):
    def __init__(self):
        self.line = "initial"

class Output(object):
    def __init__(self):
        self.line = "initial"

class Parser(object):
    def  __init__(self, file_name):
        self.file_name = file_name

    def parse(self):
        file = open(self.file_name, 'r')

        input = Input()
        input.tests = []
        for line in file.readlines()[1:]:
            logging.debug("in:" + line)
            string = line[:line.index(" ")]
            k_string = line[line.index(" "):]
            k = int(k_string)
            logging.debug("parsed:" + string + "," + str(k))
            input.tests.append(Test(string, k))

        file.close()
        return input

    def write(self, output):
        self.file = open('out_' + self.file_name, 'w')
        self.write_object(output)
        self.file.close()

    def write_object(self, output):
        logging.debug("Tests:" + str(len(output.tests)))
        for i  in range(1, len(output.tests) + 1):
            self.write_test(i, output.tests[i-1])

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
            self.flip(test)

        return output

    def flip(self, test):
        string = test.string
        k = test.k
        logging.info("=>" + string + "," + str(k))
        count = 0
        for i in range(0, len(string) - k + 1):
            if string[i] == "+":
                logging.debug("OK")
                continue
            else:
                logging.debug("FLIP")
                count = count + 1
                string = self.flip_string(string, i, k)
        if self.check_end(string, k):
            test.result = str(count)
        else:
            test.result = "IMPOSSIBLE"

    def flip_string(self, string, i, k):
        logging.debug("before:" + string)
        new_string = string[0:i]
        new_string += self.reverse(string[i: i+k])
        new_string += string[i+k:]
        logging.debug("after:" + new_string)
        return new_string

    def reverse(self, string):
        string = string.replace("+", "x")
        string = string.replace("-", "+")
        string = string.replace("x", "-")
        return string

    def check_end(self, string, k):
        end = string[len(string) - k:]
        logging.debug("end:" + end)
        try:
            end.index("-")
            return False
        except:
            return True

def main():
    parser = Parser("pancake_flipper_3_large.txt")

    out = Executor().method(parser.parse())
    parser.write(out)

if __name__ == "__main__":
    main()


