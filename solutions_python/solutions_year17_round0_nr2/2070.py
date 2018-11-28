
class TidyNumbers(object):
    def __init__(self):
        self.T = None
        self.NUMBERS = []
        self.read_input()
        self.NUM_ARRAY = []

    def read_input(self):
        self.T = int(raw_input())
        for i in xrange(1, self.T+1):
            N = str(raw_input())
            self.NUMBERS.append(N)

    def preprocess(self):
        for num in self.NUMBERS:
            digit_array = [int(c) for c in str(num)]
            self.NUM_ARRAY.append(digit_array)

    def is_array_tidy(self, array):
        prev = 0
        for a in array:
            if a >= prev:
                if 0 <= a <= 9:
                    prev = a
                else:
                    return False
            else:
                return False
        return True

    def find_fracture_point(self, array):
        prev = 0
        i = 0
        for a in array:
            if a < prev:
                return i
            prev = a
            i += 1
        return -1

    def manipulate_array(self, array, fracture_point):
        array[fracture_point-1] -= 1
        for i in range(fracture_point, len(array)):
            array[i] = 9
        return array

    def tidify(self):
        for i, ARRAY in enumerate(self.NUM_ARRAY):
            while not self.is_array_tidy(ARRAY):
                fracture_point = self.find_fracture_point(ARRAY)
                ARRAY = self.manipulate_array(ARRAY, fracture_point)
            self.NUM_ARRAY[i] = ARRAY
            # print ARRAY
            # print i, self.find_fracture_point(ARRAY)

    def postprocess(self):
        for i, ARRAY in enumerate(self.NUM_ARRAY):
            # print ARRAY
            self.NUMBERS[i] = "".join([str(c) for c in ARRAY]).lstrip("0")

    def print_stats(self):
        # print self.T
        # print self.NUMBERS

        with open("output.txt", "w") as f:
            for i, num in enumerate(self.NUMBERS):
                str =  "Case #{0}: {1}".format(i+1, num)
                print str
                f.write(str+"\n")


if __name__=="__main__":
    TNObj = TidyNumbers()
    TNObj.preprocess()
    TNObj.tidify()
    TNObj.postprocess()
    TNObj.print_stats()
