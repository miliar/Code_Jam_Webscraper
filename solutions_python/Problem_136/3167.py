"""
Start with:
  2 cookies per second
  C = cost of a farm
  F = number of cookies per second added from a farm
  X = the number of cookies to win.

Whenever you reach C, just look at the amount needed to win (X) and greedily
determine if it would be faster to continue at the current rate or to buy
another farm.
"""

class Player:

    def __init__(self, cost_of_farm, cps_added_by_farm, cookies_to_win):
        self.cookies_per_second = 2.0
        self.cost_of_farm = cost_of_farm
        self.cps_added_by_farm = cps_added_by_farm
        self.cookies_to_win = cookies_to_win
        self.seconds = 0.0

    def should_buy_farm(self):
        current_time_to_win = self.num_seconds_to_win_at_default()
        projected_time_to_win = self.num_seconds_to_win_at(self.cookies_per_second + self.cps_added_by_farm,
                                                           self.seconds + self.num_seconds_until_next_farm(),
                                                           self.cookies_to_win)
        return current_time_to_win > projected_time_to_win

    def num_seconds_to_win_at(self, cps, seconds, cookies_left_to_win):
        return seconds + (cookies_left_to_win / cps)

    def num_seconds_to_win_at_default(self):
        return self.num_seconds_to_win_at(self.cookies_per_second,
                                          self.seconds,
                                          self.cookies_to_win)

    def num_seconds_until_next_farm(self):
        """
        Continuous
        @returns: (float)
        """
        return self.cost_of_farm / self.cookies_per_second

    def buy_farm(self):
        self.seconds += self.num_seconds_until_next_farm()
        self.cookies_per_second += self.cps_added_by_farm

def parse_input():
    with open("cookie.data") as f:
        _ = f.readline()
        cases = []
        while True:
            line = f.readline()
            if not line or not line.strip():
                return cases
            numbers = map(float, line.split(" "))
            cases.append(numbers)

def get_num_seconds_to_win(player):
    while True:
        if not player.should_buy_farm():
            return player.num_seconds_to_win_at_default()
        player.buy_farm()

def output(case, seconds_to_win):
    with open('cookie.out', 'a') as f:
        text = "Case #" + str(case) + ": " + str(seconds_to_win)
        f.write(text + "\n")

def main():
    cases = parse_input()
    for i, case in enumerate(cases):
        cost_of_farm, cps_added_by_farm, cookies_to_win = case
        player = Player(cost_of_farm, cps_added_by_farm, cookies_to_win)
        seconds_to_win = get_num_seconds_to_win(player)
        output(i + 1, seconds_to_win)

if __name__ == "__main__":
    main()
