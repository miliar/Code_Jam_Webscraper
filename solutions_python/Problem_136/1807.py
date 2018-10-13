
# File handles
input_file = open('B-large.in', 'r')
output_file = open('B-large.out', 'w')


# Function solves one game
def SolveOneGame(caseNumber):
    line = input_file.readline()
    game_data = line.split()
    farm_cost = float(game_data[0])
    farm_production = float(game_data[1])
    cookies_needed = float(game_data[2])

    time_used_for_building = 0.0
    current_production = 2.0

    last_round_time_needed = cookies_needed / current_production

    notFound = True
    while notFound:
        # add a farm
        time_used_for_building = time_used_for_building + farm_cost / current_production
        current_production = current_production + farm_production
        time_to_get_needed_value = cookies_needed / current_production
        all_time_for_current = time_used_for_building + time_to_get_needed_value 

        if all_time_for_current > last_round_time_needed:
            output_file.write("Case #" + str(caseNumber) + ": " + str(round(last_round_time_needed, 7)) + "\n")
            notFound = False
        else:
            last_round_time_needed = all_time_for_current

# The main logic
number_of_games = int(input_file.readline())
for g in range(0, number_of_games):
    SolveOneGame(g + 1)


# Close the files
input_file.close()
output_file.close()