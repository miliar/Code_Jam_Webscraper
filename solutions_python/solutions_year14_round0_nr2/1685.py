class Solver(object):
    def __init__(self, cost, farm_cookies, target):
        self.cost = cost
        self.farm_cookies = farm_cookies
        self.target = target
        self.best_so_far = target/2.0

    def seconds_with_n_farms(self, n):
        farms = 0
        cookies_per_second = 2.0
        seconds = 0.0
        for i in range(n):
            seconds += self.cost / cookies_per_second
            farms += 1
            cookies_per_second += self.farm_cookies
        return self.target/cookies_per_second + seconds

    def solve(self):
        farms = 1
        seconds = self.seconds_with_n_farms(farms)
        while seconds < self.best_so_far:
            self.best_so_far = seconds
            farms += 1
            seconds = self.seconds_with_n_farms(farms)
        return self.best_so_far

f = open('test.txt')
num_cases = int(f.readline())

out = open('out.txt', 'w')

for i in range(num_cases):
    cost, farm_cookies, target = [float(n) for n in f.readline().strip().split(' ')]
    s = Solver(cost, farm_cookies, target)
    out.write("Case #%d: %f\n" % (i+1, s.solve()))