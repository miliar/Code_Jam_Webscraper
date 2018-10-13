# Nadeem Malik

import sys

with open(sys.argv[1]) as f:
    content = f.readlines()

output_file = open(sys.argv[2], 'w')

num_tests = int(content[0]);

if(num_tests >= 1 and num_tests <= 100):
	line_idx = 1;
	tests_done = 1;

	while(tests_done <= num_tests):
		sec = 0.0;
		c = 0.0;
		f = 2.0;	
		farm_cost = float(list(content[line_idx].rstrip().split(" "))[0]);
		farm_rate_bonus = float(list(content[line_idx].rstrip().split(" "))[1]);
		cookies_goal = float(list(content[line_idx].rstrip().split(" "))[2]);

		#print("farm cost, farm_rate_bonus, cookies_goal: " + str(farm_cost) + ", " + str(farm_rate_bonus) + ", " + str(cookies_goal) + "\n");
		while(c < cookies_goal):
			# time until we can buy a farm plus time left to reach cookie goal
			# after getting the farm bonus
			#print("num cookies " + str(c));

			# seconds to get farm, seconds to get cookies left after farm bonus
			t_f = (farm_cost / f) + ((cookies_goal - c) / (f + farm_rate_bonus))

			# seconds left to get cookies at current rate
			t_x = (cookies_goal - c) / f; # this is the time if we just wait until the cookies goal
										  # and do not buy a farm
			min_time_needed = min(t_f, t_x);

			#print("t_f: " + str(t_f) + " t_x:" + str(t_x));
			
			# check if we should buy the farm
			if(min_time_needed == t_x):
				# wait
				sec += t_x;
				c += (t_x * f);
			else:
				# wait until we can buy a farm
				# cookies left to get farm / rate
				t_f = (farm_cost - c) / f;
				#print("time until farm: " + str(t_f));

				c += f * t_f;
				sec += t_f;

				c -= farm_cost;
				f += farm_rate_bonus;


		#print("total time: " + str(sec))
		output_file.write("Case #" + str(tests_done) + ": " + str(sec) + "\n");

		line_idx += 1;
		tests_done += 1;
