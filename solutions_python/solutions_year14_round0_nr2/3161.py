FARM_COST_INDEX = 0
FARM_RATE_INDEX = 1
WIN_COST_INDEX = 2
MAX_FARMS = 100000
def processFile(filename):
	in_file = open(filename,"r")
	number_of_games = int(in_file.readline())
	#get the parameters
	for game_index in range(number_of_games):
		params = [float(x) for x in in_file.readline().split()]
		farm_cost = params[FARM_COST_INDEX]
		farm_rate = params[FARM_RATE_INDEX]
		win_cost = params[WIN_COST_INDEX]
		time_to_win_no_farms = win_cost/2.0
		last_time_to_win = time_to_win_no_farms
		optimal_number_of_farms = 0
		time_spent_producing_farms = 0
		for i in range(1,MAX_FARMS):
			time_spent_producing_farms += farm_cost/(2.0+(i-1)*farm_rate)
			time_to_win = time_spent_producing_farms + win_cost/(2.0+i*farm_rate)
			if(time_to_win > last_time_to_win):
				optimal_number_of_farms = i-1
				break
			else:
				last_time_to_win = time_to_win
		else:
			print "ERROR"
		time_spent_producing_farms -= farm_cost/(2.0+(optimal_number_of_farms)*farm_rate)
		time_to_win = time_spent_producing_farms + win_cost/(2.0+optimal_number_of_farms*farm_rate)
		string ="Case #"+str(game_index+1)+": "+str(round(time_to_win,7))
		print string


if __name__ == "__main__":
	processFile("B-large.in")
