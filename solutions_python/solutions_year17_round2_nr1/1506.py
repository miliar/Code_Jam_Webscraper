import sys


f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'w')

lines = f.readlines()

f.close()

N = int(lines[0].strip())

case_no = 0

i = 1

while i < len(lines):
		case_no += 1
		print "case no: " + str(case_no)
		D = int(lines[i].split(" ")[0])
		H = int(lines[i].split(" ")[1])
		print "target distance: " + str(D)
		print "number of horses: " + str(H)
		longest_time = 0
		#slowest_horse = []
		for j in range(i+1, i+H+1):
			horse_start = int(lines[j].split(" ")[0])
			horse_speed = int(lines[j].split(" ")[1])*1.0
			time_taken = (D-horse_start)/horse_speed
			print "horse_start: " + str(horse_start)
			print "horse speed: " + str(horse_speed)
			print "time_taken: " + str(time_taken)
			if time_taken > longest_time:
				longest_time = time_taken
				print "longest_time was replaced with: " + str(longest_time)
		if longest_time != 0:
			speed = D/longest_time
			print "speed is: " + str(speed)
		else:
			print "division by zero test case makes no sense: " + str(D) 
		i += H+1
		g.write("Case #" + str(case_no) + ": " + str(speed) + "\n")

g.close()
