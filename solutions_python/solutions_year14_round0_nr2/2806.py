def calculate(thecost, increase_rate, final_thecost, current_rate = 2.0, elapsed_time = 0.0, elapsed_thecost = 0.0):
	time1 = (final_thecost - elapsed_thecost)/current_rate
	farming_time = thecost/current_rate
	time2 = farming_time + (final_thecost - elapsed_thecost)/(current_rate + increase_rate)
	while time1>=time2:
		elapsed_time += farming_time
		elapsed_thecost = 0
		current_rate += increase_rate
		time1 = (final_thecost - elapsed_thecost)/current_rate
		farming_time = thecost/current_rate
		time2 = farming_time + (final_thecost - elapsed_thecost)\
		/(current_rate + increase_rate)
	if time1<time2:
		elapsed_time += time1
		elapsed_thecost = final_thecost
		return elapsed_time


fin = open("data.in","r")
cases = fin.readline()
cases = int(cases[:-1])
fout = open("data.out","w+")

for i in range(cases):
	row = fin.readline()[:-1]
	row = row.split(" ")
	row = map(float, row)
	final_time = calculate(row[0], row[1], row[2])
	final_answer = "Case #" + `i+1` + ": " + `final_time` + "\n"
	fout.write(final_answer)
