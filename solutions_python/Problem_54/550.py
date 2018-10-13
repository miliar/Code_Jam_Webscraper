import sys

sys.setrecursionlimit(20000)

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def mgcd(numbers):
    if len(numbers)==0:
        return 1
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return gcd(numbers[0], numbers[1])
    else:
        return mgcd([gcd(numbers[0], numbers[1])] + numbers[2:])

def qgcd(numbers):
    nums = []
    a = numbers[0]
    nums.extend([abs(n - a) for n in numbers[1:] if n != a])
    nums = list(set(nums))
    return mgcd(nums)

class TestInput(object):
    def __init__(self, input_stream):
        self.input_stream = input_stream
    def readline(self):
        return self.input_stream.readline().strip()
    def read(self, *args):
        words = self.readline().split()
        result = []
        for i in range(len(args)):
            result.append(args[i](words[i]))
        if len(args) == 1:
            return result[0]
        return result
    def read_list(self, atype):
        words = self.readline().split()
        return map(atype, words)

class FairWarningCase(TestInput):
    def __init__(self, input_stream):
        super(FairWarningCase, self).__init__(input_stream)
        nums = self.read_list(long)
        numbers = list(set(nums[1:]))
        T = qgcd(numbers)
        y = -numbers[0] % T
        self.result=str(y)


class FairWarningTester(TestInput):
    def __init__(self, input_stream):
        super(FairWarningTester, self).__init__(input_stream)
        C = self.read(int)
        for c in range(C):
            sys.stderr.write("Case #%d/%d\n"%(c+1,C))
            case = FairWarningCase(input_stream)
            print "Case #%d: %s" % (c+1, case.result)

fwt=FairWarningTester(sys.stdin)

