__author__ = 'hansihe'

import reader
import time

input_reader = reader.read_test_file(open('input', 'r'), reader.fixed_length_case_reader())


class GameState(object):

    def __init__(self, farm_cost, farm_production):
        self.farm_cost = farm_cost
        self.farm_production = farm_production

        self.cookies = 0
        self.farms = 0

        self.time_passed = 0

    @property
    def cps(self):
        return 2.0 + (self.farms * self.farm_production)

    def buy_farm(self):
        if self.cookies >= self.farm_cost:
            self.farms += 1
            self.cookies -= self.farm_cost
            return True
        raise Exception("Farm buy error")

    def time_until(self, cookies, cps=None):
        return cookies / (cps or self.cps)

    def simulate_time(self, seconds):
        self.cookies += round(self.cps * seconds, 10)
        self.time_passed += seconds

    def simulate_until_cookies(self, cookies):
        self.simulate_time(self.time_until(cookies))


def run_game(game_state, win_score, case_num):
    while True:
        if game_state.time_until(win_score) <= (game_state.time_until(game_state.farm_cost) + game_state.time_until(win_score, game_state.cps + game_state.farm_production)):
            game_state.simulate_until_cookies(win_score)
            return game_state.time_passed
        else:
            game_state.simulate_until_cookies(game_state.farm_cost)
            game_state.buy_farm()


for case_p in input_reader:
    case_num, case_data = case_p
    farm_cost, farm_production, win_score = [float(x) for x in case_data[0].split(" ")]
    result = run_game(GameState(farm_cost, farm_production), win_score, case_num)
    print("Case #" + str(case_num) + ": " + str(round(result, 7)))