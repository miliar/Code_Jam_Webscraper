__author__ = 'Gauthier'

class CookieCase(object):
    def __init__(self, params):
        self.farm_cost = params[0]
        self.farm_prod = params[1]
        self.win_cost = params[2]
        self.prod_rate = 2.0
        self.elapsed_time = 0.0

    def check_victory_time(self, prod_rate):
        return self.win_cost / prod_rate

    def check_farm_time(self):
        return self.farm_cost / self.prod_rate

    def resolve(self):
        while True:
            vic_time_needed = self.check_victory_time(self.prod_rate)
            farm_time_needed = self.check_farm_time()
            if vic_time_needed <= farm_time_needed + self.check_victory_time(self.prod_rate + self.farm_prod):
                self.elapsed_time += vic_time_needed
                break
            else:
                self.elapsed_time += farm_time_needed
                self.prod_rate += self.farm_prod
        return self.elapsed_time

class CookieClicker(object):
    def read_input(self):
        fd = open("input.txt")
        lines = fd.readlines()
        self.nb_test_case = int(lines[0])
        lines = lines[1:]
        self.test_cases = []
        for i in range(self.nb_test_case):
            self.test_cases.append(CookieCase(map(float, lines[i].strip().split(' '))))
        fd.close()

def main():
    cc = CookieClicker()
    cc.read_input()
    output = open('output.txt', "w+")
    for i in range(len(cc.test_cases)):
        tc = cc.test_cases[i]
        output.write("Case #%d: %.7f\n" % (i + 1, tc.resolve()))
    output.close()

if __name__ == "__main__":
    main()