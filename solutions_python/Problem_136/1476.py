input = open("2input", "r")
output = open("2output", "w")

def readline():
	return input.readline()

def writeline(string):
	output.write(string + "\n")

def calculate_time(from_clicks, from_farms, need, cur):
	return (need - cur)/(from_clicks + from_farms)

def decide_spend(cost, cookies, need, current_farms, boost_per_farm):
	t1 = calculate_time(2.0, current_farms*boost_per_farm, need, cookies)
	t2 = calculate_time(2.0, (current_farms+1)*boost_per_farm, need, 0.0)

	return t2 < t1

def main():
	count = int(readline())
	for i in range(count):
		line = readline().replace("\n", "").split(" ")

		c = float(line[0])
		f = float(line[1])
		x = float(line[2])

		k = 0
		t = 0
		while decide_spend(c, c, x, k, f):
			t += c/(k*f + 2)
			k += 1

		t += x/(k*f + 2)

		writeline("Case #" + str(i + 1) + ": " + str(t))

main()
