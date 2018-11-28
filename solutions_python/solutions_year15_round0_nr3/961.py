class Quaternions(object):
    def __init__(self, val):
        self.value = val

    @staticmethod
    def __multiply(a, b):
        minus = False
        if a[0] == '-':
            minus = True
            a = a[1:]
        if b[0] == '-':
            if not minus:
                minus = True
            else:
                minus = False
            b = b[1:]
        if a == '1':
            if minus:
                return Quaternions('-'+b)
            else:
                return Quaternions(b)
        if b == '1':
            if minus:
                return Quaternions('-'+a)
            else:
                return Quaternions(a)

        if a == b:
            if minus:
                return Quaternions('1')
            else:
                return Quaternions('-1')

        if a == 'i':
            if b == 'j':
                if minus:
                    return Quaternions('-k')
                else:
                    return Quaternions('k')
            if b == 'k':
                if minus:
                    return Quaternions('j')
                else:
                    return Quaternions('-j')
        if a == 'j':
            if b == 'i':
                if minus:
                    return Quaternions('k')
                else:
                    return Quaternions('-k')
            if b == 'k':
                if minus:
                    return Quaternions('-i')
                else:
                    return Quaternions('i')

        if a == 'k':
            if b == 'i':
                if minus:
                    return Quaternions('-j')
                else:
                    return Quaternions('j')
            if b == 'j':
                if minus:
                    return Quaternions('i')
                else:
                    return Quaternions('-i')

    def __mul__(self, other):
        return Quaternions.__multiply(self.value, other.value)



class Case(object):
    def __init__(self, data):
        self.data = data

    def solve(self):

        if self.compute_string(self.data).value != '-1':
            return 'NO'

        for i in xrange(len(self.data) - 1):
            if self.compute_string(self.data[0:i]).value == 'i':
                val = Quaternions('1')
                for j in xrange(i, len(self.data)):
                    val *= Quaternions(self.data[j])
                    if val.value == 'j':
                        return 'YES'
        return 'NO'

    def compute_string(self, data):
        val = Quaternions('1')
        for x in data:
            val *= Quaternions(x)

        return val

def parse_stdin():
    T = int(raw_input())
    cases = []
    for i in xrange(T):
        X = int(raw_input().split(' ')[1])
        data = raw_input()*X
        data = [x for x in data]
        cases.append(Case(data))
    return cases


def main():
    cases = parse_stdin()
    i = 1
    for c in cases:
        print 'Case #{:d}:'.format(i), c.solve()
        i += 1


if __name__ == '__main__':
    main()
