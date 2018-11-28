class TestCase(object):
    def __init__(self):
        super(TestCase, self).__init__()
        self.first_tab = []
        self.first_resp = 0
        self.second_tab = []
        self.second_resp = 0

    def resolve(self):
        res = []
        for i in self.first_tab[self.first_resp - 1]:
            for j in self.second_tab[self.second_resp - 1]:
                if i == j:
                    res.append(j)
        return res

class MagicTrick(object):
    def read_input(self):
        fd = open("input.txt")
        lines = fd.readlines()
        self.nb_test_case = int(lines[0])
        lines = lines[1:]
        self.test_cases = []
        for i in range(self.nb_test_case):
            t = TestCase()
            self.test_cases.append(t)
            t.first_resp = int(lines[0])
            lines = lines[1:]
            for i in range(4):
                t.first_tab.append(lines[i].strip().split(' '))
            lines = lines[4:]
            t.second_resp = int(lines[0])
            lines = lines[1:]
            for i in range(4):
                t.second_tab.append(lines[i].strip().split(' '))
            lines = lines[4:]
        fd.close()

def main():
    mt = MagicTrick()
    mt.read_input()
    output = open("output.txt", "w+")
    for i in range(len(mt.test_cases)):
        tc = mt.test_cases[i]
        res = tc.resolve()
        output.write("Case #%d: " % (i + 1))
        if len(res) == 1:
            output.write("%d\n" % int(res[0]))
        elif len(res) == 0:
            output.write("Volunteer cheated!\n")
        else:
            output.write("Bad magician!\n")

    output.close()

if __name__ == "__main__":
    main()