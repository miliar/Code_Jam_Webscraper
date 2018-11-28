#!/usr/bin/python

###
# Definitions and files to open
###
out_array = []
source_file = 'Q2.txt'

try:
    f = open(source_file)
except IOError:
    print ('could not open source file ' + source_file)

###
# Classes we need
###
class Game:
    def __init__(self, cc, ff, xx):
        self.cost = cc
        self.farm_speed = ff
        self.win_con = xx
        # Column a represents what would happen if you bought the first a farms
        self.current_cookies_by_farms = [0.0]
        self.cookie_rate_by_farms = [2.0]
        self.elapsed_time = 0.0

    def evaluate(self):
        max_farms = 0
        done = False
        total_times = []
        ###
        # The intention is to keep incrementing the current_cookies_by_farms
        # until one of then exceeds win_con, then decrement that one to find
        # when we won.
        ###
        # Start by checking if we've already won!
        while not done:
            # Work out how long it'll take to get the next farm
            current_rate = self.cookie_rate_by_farms[-1]
            next_farm_time = self.cost/current_rate

            # Document the buying of the next farm: we click for next_farm_time
            # to get enough cookies, we enter a hypothetical universe in which
            # we buy a new farm using cookies, and our cookie rate increases.  
            self.elapsed_time += next_farm_time
            max_farms += 1            

            # See how many cookies we would have by now in all our hypothetical
            # farms
            for ii in range(max_farms):
                increment = self.cookie_rate_by_farms[ii] * next_farm_time
                self.current_cookies_by_farms[ii] += increment
                # Check if we've won yet
                if self.current_cookies_by_farms[ii] >= self.win_con:
                    # We've won! Find out when.
                    done = True
                    over_num = self.current_cookies_by_farms[ii] - self.win_con
                    over_time = over_num/self.cookie_rate_by_farms[ii]
                    total_time = self.elapsed_time - over_time
                    total_times.append(total_time)

            if done == True:
                # We've won! Return the fastest time and get out.
                return min(total_times)

            # If we get here, we've not won yet. Create a new universe in which
            # we buy another farm.
            self.current_cookies_by_farms.append(
                self.current_cookies_by_farms[-1] - self.cost)
            new_rate = current_rate + self.farm_speed
            self.cookie_rate_by_farms.append(new_rate)
            # Round the loop we go!

    def play(self, num):
        result = self.evaluate()
        out_str = 'Case #' + str(num + 1) + ': ' + str(result)
        return out_str

###
# Parse the input and play the games
###

num_games = int(f.readline().rstrip())

for ii in range(num_games):
    print('game ' + str(ii))
    game_input = [float(jj) for jj in f.readline().rstrip().split()]
    new_game = Game(game_input[0], game_input[1], game_input[2])
    out_array.append(new_game.play(ii))

###
# Print the results
###

for out_line in out_array:
    print(out_line)
