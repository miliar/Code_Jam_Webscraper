import pandas as pd
import sys

input_string = sys.argv[1]

input_data = pd.read_csv(input_string, header=None)

number_of_cases = input_data.iloc[0]
input_data = input_data.drop(0).reset_index(drop=True)

output_list = []
for i in range(0, number_of_cases):
    (C, F, X) = [float(x) for x in input_data.iloc[0].values[0].split()]
    input_data = input_data.drop(0).reset_index(drop=True)
    
    base_rate = 2.0
    
    # Time to Cookie Farm
    cookie_farm_time = C / base_rate
    
    # Time to Goal
    N = 1
    time_to_goal = X / base_rate
    print('C: ' + str(C) + ' F: ' + str(F) + ' X: ' + str(X))
    while True:
        augmented_rate = base_rate + N*F
        time_to_goal_augmented = cookie_farm_time + X/augmented_rate
        print('Goal: ' + str(X) + ' No Add: ' + str(time_to_goal) + ' Add: ' + str(time_to_goal_augmented))
        if time_to_goal <= time_to_goal_augmented:
            output = time_to_goal
            break
        else:
            time_to_goal = time_to_goal_augmented
            cookie_farm_time += C / augmented_rate
            N+=1
    output_list.append(output)

output_list = ['Case #' + str(num+1) + ': ' + str(x) for (num, x) in enumerate(output_list)]
output = pd.DataFrame(output_list)
output.to_csv('output', header=False, index=False)