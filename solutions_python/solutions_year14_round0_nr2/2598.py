from __future__ import print_function

__author__ = 'shreyas kulkarni (shyran@gmail.com)'

class CookieClicker(object):
    def __init__(self, farm_cost, cookies_per_farm, target):
        self.C = farm_cost
        self.X = target
        self.F = cookies_per_farm

    def __call__(self, *args, **kwargs):
        return self.get_best_time_iteratively(2)

    def get_best_time_iteratively(self, initial_production_rate):
        accumulated_time = 0.0
        accumulated_production_rate = initial_production_rate

        while True:
            time_if_farm_not_bought = accumulated_time + float(self.X / accumulated_production_rate)

            accumulated_time += float(self.C / accumulated_production_rate)
            accumulated_production_rate += self.F

            time_if_farm_bought = accumulated_time + float(self.X / accumulated_production_rate)

            if time_if_farm_bought >= time_if_farm_not_bought:
                return time_if_farm_not_bought


import fileinput
input_lines = [line.strip() for line in fileinput.input()]

for idx, line in enumerate(input_lines[1:]):
    print("Case #%d: %.7f" % (idx + 1, CookieClicker(*[float(x) for x in line.split()])()))