def calc(cost, increase_rate, final_cost, current_rate = 2.0, elapsed_time = 0.0, elapsed_cost = 0.0):
	time1 = (final_cost - elapsed_cost)/current_rate
	farming_time = cost/current_rate
	time2 = farming_time + (final_cost - elapsed_cost)/(current_rate + increase_rate)
	while time1>=time2:
		elapsed_time += farming_time
		elapsed_cost = 0
		current_rate += increase_rate
		time1 = (final_cost - elapsed_cost)/current_rate
		farming_time = cost/current_rate
		time2 = farming_time + (final_cost - elapsed_cost)/(current_rate + increase_rate)
	if time1<time2:
		elapsed_time += time1
		elapsed_cost = final_cost
		return elapsed_time

fin = open("input.in","r")
cases = fin.readline()
cases = int(cases[:-1])
fout = open("data.out","w+")

for i in range(cases):
	row = fin.readline()[:-1]
	row = row.split(" ")
	row = map(float, row)
	final_time = calc(row[0], row[1], row[2])
	final_answer = "Case #" + `i+1` + ": " + `final_time` + "\n"
	fout.write(final_answer)

fout.close()
