from sys import stdin, stdout

class Solver :

    def run(self) :
        caseNum = int(stdin.readline())
        for caseIndex in range(caseNum) :
            self.input()
            self.exe()
            self.output(caseIndex + 1)

    def input(self) :
        self.N, self.R, self.P, self.S = (int(_) for _ in stdin.readline().split())

    def exe(self) :
        oper = ['P', 'R', 'S']
        self.length = 1 << self.N
        self.result = []
        for code in range(3 ** self.length) :
            order = []
            tmp = code
            counts = [0, 0, 0]
            for i in range(self.length) :
                r = tmp % 3
                tmp /= 3
                order.append(oper[r])
                counts[r] += 1
            if counts[0] == self.P and counts[1] == self.R and counts[2] == self.S :
                if self.check(order) :
                    if len(self.result) == 0 or self.result > order :
                        self.result = order

    def check(self, order) :
        tmp = order[:]
        while len(tmp) > 1 :
            tmp1 = []
            for i in range(len(tmp) >> 1) :
                a = tmp[i * 2]
                b = tmp[i * 2 + 1]
                if a == b :
                    return False
                if a == 'P' and b == 'R' :
                    c = 'P'
                elif a == 'P' and b == 'S' :
                    c = 'S'
                elif a == 'R' and b == 'P' :
                    c = 'P'
                elif a == 'R' and b == 'S' :
                    c = 'R'
                elif a == 'S' and b == 'P' :
                    c = 'S'
                elif a == 'S' and b == 'R' :
                    c = 'R'

                tmp1.append(c)
            tmp = tmp1
        return True

    def output(self, caseIndex) :
        stdout.write("Case #%d: " % (caseIndex))
        if len(self.result) == 0 :
            stdout.write("IMPOSSIBLE\n")
        else :
            stdout.write("%s\n" % ("".join(self.result)))

if __name__ == "__main__" :
    instance = Solver()
    instance.run()

