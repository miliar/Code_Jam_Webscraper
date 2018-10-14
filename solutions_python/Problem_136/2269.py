def time_claculator(farm_cost, increase_rate, final_cost, current_rate = 2.0, elapsed_time = 0.0, elapsed_cost = 0.0):
	time1 = (final_cost - elapsed_cost)/current_rate
	farming_time = farm_cost/current_rate
	time2 = farming_time + (final_cost - elapsed_cost)/(current_rate + increase_rate)
	while time1>=time2:
		elapsed_time += farming_time
		elapsed_cost = 0
		current_rate += increase_rate
		time1 = (final_cost - elapsed_cost)/current_rate
		farming_time = farm_cost/current_rate
		time2 = farming_time + (final_cost - elapsed_cost)/(current_rate + increase_rate)
	if time1<time2:
		elapsed_time += time1
		elapsed_cost = final_cost
		return elapsed_time

fin = open("data.in","r")
test_cases = fin.readline()
test_cases = int(test_cases[:-1])
fout = open("data.out","w+")

for i in range(test_cases):
	row = fin.readline()[:-1]
	row = row.split(" ")
	row = map(float, row)
	final_time = time_claculator(row[0], row[1], row[2])
	final_answer = "Case #" + `i+1` + ": " + `final_time` + "\n"
	fout.write(final_answer)

fout.close()
