REAL_1 = 0
IMAG_I = 1
IMAG_J = 2
IMAG_K = 3

Q_MULT = [[REAL_1, IMAG_I, IMAG_J, IMAG_K],
          [IMAG_I, REAL_1, IMAG_K, IMAG_J],
          [IMAG_J, IMAG_K, REAL_1, IMAG_I],
          [IMAG_K, IMAG_J, IMAG_I, REAL_1]
         ]
Q_MULT_SIGN = [[1,  1,  1,  1],
               [1, -1,  1, -1],
               [1, -1, -1,  1],
               [1,  1, -1, -1]
              ]

char2imagtype = {'i': IMAG_I,
                 'j': IMAG_J,
                 'k': IMAG_K }

imagtype2char = {IMAG_I: 'i',
                 IMAG_J: 'j',
                 IMAG_K: 'k',
                 REAL_1: '1', }


class Quaternion:
    @classmethod
    def create(cls, char):
        return cls(char2imagtype[char])

    def __init__(self, imag_type, sign=1):
        self.sign = sign
        self.imag_type = imag_type

    def __mul__(self, other):
        new_imag_type = Q_MULT[self.imag_type][other.imag_type]
        new_sign = self.sign * other.sign * Q_MULT_SIGN[self.imag_type][other.imag_type]
        return Quaternion(new_imag_type, new_sign)

    def isI(self):
        return self.sign == 1 and self.imag_type == IMAG_I

    def isJ(self):
        return self.sign == 1 and self.imag_type == IMAG_J

    def isK(self):
        return self.sign == 1 and self.imag_type == IMAG_K

    def __repr__(self):
        return "<Q {}>".format(str(self))

    def __str__(self):
        txt = imagtype2char[self.imag_type]
        if self.sign==-1:
            return "-"+txt
        else:
            return txt


def testQuaternion():
    _i = Quaternion.create('i')
    _j = Quaternion.create('j')
    _k = Quaternion.create('k')
    assert (_j * _i * _j).isI()
    assert (_k * _i * _i * _j).isI()
    assert (_j*_j).sign == -1
    assert str(_k * _k * _k * _k) == "1"


def reduceTillI(numbers):
    current = None
    for i, number in enumerate(numbers):
        if i == 0:
            current = number
        else:
            current = current * number
        if current.isI():
            #print("reduceTillI: "+str(i))
            yield numbers[i+1:]

def reduceTillJ(numbers):
    current = None
    for i, number in enumerate(numbers):
        if i == 0:
            current = number
        else:
            current = current * number
        if current.isJ():
            yield numbers[i+1:]

def reduceAll(numbers):
    if len(numbers) == 0:
        return Quaternion(REAL_1)

    x = numbers[0]
    for y in numbers[1:]:
        x = x * y
    return x

class Case:
    @classmethod
    def parse(cls, stream):
        line1 = next(stream).strip()
        line2 = next(stream).strip()

        charsCount, repeat = map(int, line1.split(' '))
        line2 *= repeat

        numbers = map(Quaternion.create, line2)
        return cls(list(numbers))

    def __init__(self, numbers):
        self.numbers = numbers

    def solve(self):
        numbers = self.numbers
        total = reduceAll(numbers)

        if total.sign != -1 or total.imag_type != REAL_1:
            return False

        for tail1 in reduceTillI(numbers):
            for tail2 in reduceTillJ(tail1):
                if reduceAll(tail2).isK():
                    return True
        return False


def main(finname, foutname=None):
    fin = open(finname, 'r')
    fout = None if foutname==None else open(foutname, 'w')
    count = int(next(fin).strip())
    for i in range(count):
        case = Case.parse(fin)
        answer = "YES" if case.solve() else "NO"
        print("Case #{}: {}".format(i+1, answer), file=fout)

if __name__ == '__main__':
    testQuaternion()
    main("C-small-attempt0.in", "C-small-attempt0.out")
