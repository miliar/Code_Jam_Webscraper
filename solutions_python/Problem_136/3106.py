class Cookie():
    def __init__(self, to_farm, objective, farm_rate):
        self.to_farm = to_farm
        self.farm_rate = farm_rate
        self.total_cookies = 0
        self.objective = objective
        self.rate = 2
        self.time_spent = 0

    def time_to_objective(self, rate=None):
        if not rate:
            rate = self.rate
        return float(self.objective - self.total_cookies) / rate

    def time_to_farm(self):
        return float(self.to_farm - self.total_cookies) / self.rate

    def pos_farm_to_objective(self):
        ttf = self.time_to_farm()
        tto = self.time_to_objective(self.rate + self.farm_rate)
        return ttf + tto

    def buy_farm(self):
        self.time_spent += self.time_to_farm()
        self.rate += self.farm_rate


def calc_time(farm_rate, to_farm, objective):
    ck = Cookie(to_farm, objective, farm_rate)
    while ck.objective != ck.total_cookies:
        if ck.time_to_objective() > ck.pos_farm_to_objective():
            ck.buy_farm()
        else:
            ck.time_spent += ck.time_to_objective()
            ck.total_cookies = ck.objective
    return ck.time_spent


def read_line(f):
    line = f.readline()
    args = [float(x) for x in line.split()]
    return args


def main(f_path):
    f = open(f_path, 'r')
    test_cases = int(f.readline())
    for i in range(test_cases):
        to_farm, farm_rate, objective = read_line(f)
        result = calc_time(farm_rate, to_farm, objective)
        print "Case #{0}: {1}".format(i + 1, result)


if __name__ == "__main__":
    import sys
    f_path = sys.argv[1]
    main(f_path)
