import sys

def cookie(filename):
	lines = open(filename).read().splitlines()
	f = open('cookie.out','w')

	num_cases = int(lines[0])
	for i in range(num_cases):
		data = str.split(lines[i+1], " ")
		cost = float(data[0])
		farm = float(data[1])
		goal = float(data[2])
		f.write("Case #" + str(i+1) + ": " + str(calculate(cost,farm,goal)) + "\n")

	f.close()

def calculate(cost, farm, goal):
	currentrate = 2
	t = 0

	while True:
		currenttime = t + (goal)/currentrate
		nexttime = t + (cost/currentrate) + (goal)/(currentrate+farm)
		if (currenttime > nexttime):
			t = t + (cost/currentrate)
			currentrate = currentrate + farm
		else:
			return currenttime

def main():
	cookie(sys.argv[1])

if __name__ == "__main__":
    main()