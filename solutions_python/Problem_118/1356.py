import sys
import math

def is_square(integer):
    root = math.sqrt(integer)
    nice_root = int(root + 0.5)
    nice_int = nice_root ** 2
    if nice_int == integer: 
        return nice_root
    else:
        return 0

def is_poly(number):
    s = str(number)
    l = len(s) / 2
    return s[:l] == s[::-1][:l]

class TestCase(object):

    def __init__(self, a,b):
        self.a = a
        self.b = b
        self.solution = 0

    def calc_solution(self):

        print "IN CALC SOL:", self.a, self.b


        # if a < 10 :(
        if self.a < 10:

            for i in xrange(self.a, min(10, self.b+1)):
                if i in [1,4,9]:
                    self.solution += 1
            if self.b < 10:
                return self.solution
            else:    
                start_number = 10
        else: 
            start_number = self.a

        len_a = len(str(start_number))
        i = len_a
        while True:
            if i % 2 == 1:
                if not self._calc_odd_len(start_number):
                    break
            elif i % 2 == 0:
                if not self._calc_even_len(start_number):
                    break

            start_number = 10** i
            print start_number
            i += 1

        print "Res:", self.solution
        return self.solution


    def _calc_odd_len(self, start_number):
        start_number_str = str(start_number)
        start_number_len = len(start_number_str)
        if start_number_len % 2 != 1:
            print "OMG!!!", start_number
            return True

        # get poly start
        poly_start = int(start_number_str[:start_number_len / 2])
        # calc poly_start max number
        poly_stop = 10 ** (start_number_len / 2)

        # calc the next even polinom above start, and under b
        print poly_start, poly_stop
        i = poly_start
        while i < poly_stop:
            for j in xrange(0, 10):
                poly = int(str(i) + str(j) + str(i)[::-1])
                print poly

                if poly > self.b:
                    return False
                if poly < self.a:
                    continue

                root = is_square(poly)
                if root != 0:
                    if is_poly(root):
                        self.solution += 1
                        print root, poly

            i+=1

        return True

    def _calc_even_len(self, start_number):

        start_number_str = str(start_number)
        start_number_len = len(start_number_str)
        if start_number_len % 2 != 0:
            print "OMG!!!", start_number
            return True

        # get poly start
        poly_start = int(start_number_str[:start_number_len / 2])

        # calc poly_start max number
        poly_stop = 10 ** (start_number_len / 2)

        # calc the next even polinom above start, and under b
        i = poly_start
        while i < poly_stop:
            poly = int(str(i) + str(i)[::-1])

            if poly > self.b:
                return False
            if poly < self.a:
                i += 1
                continue

            root = is_square(poly)
            if root != 0:
                if is_poly(root):
                    self.solution += 1
                    print root, poly

            i += 1

        return True



def write_output_file(output_path, outputs):
    
    output_file = open(output_path, 'wb')
    for i, res in enumerate(outputs):
        output_file.write("Case #%d: %d\n" % (i + 1, res))
    output_file.close()

def read_input_file(input_path):

    inputs = []
    input_file = open(input_path, 'rb')
    lines = input_file.readlines()
    test_cases = long(lines[0])

    for case in xrange(test_cases):
        params = lines[case + 1].split()
        inputs.append(TestCase(int(params[0]), int(params[1])))
    return inputs

def calc_outputs(inputs):
    outputs = []
    for i, case in enumerate(inputs):
        outputs.append(case.calc_solution())
    return outputs

def main():
    
    input_file = sys.argv[1]
    output_file = sys.argv[1] + ".out"
    
    inputs = read_input_file(input_file)
    outputs = calc_outputs(inputs)
    write_output_file(output_file, outputs)
    

if '__main__' == __name__:
    main()
