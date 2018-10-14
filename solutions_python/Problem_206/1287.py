filename = "A-large (1).in"
outf = file(filename + ".out", "w")
rows = [i.strip() for i in file(filename).readlines()]



def get_row():
	global rows
	temp = rows[0]
	rows = rows[1::]
	return temp



num_cases = int(get_row())


for i in range(num_cases):
	#parse case
	dest, other_horses_num = get_row().split(" ")
	dest = float(dest)
	other_horses_num = int(other_horses_num)

	max_steps = 0

	for j in range(other_horses_num):
		start, speed = get_row().split(" ")
		start = float(start) * 1.0
		speed = float(speed) * 1.0
		if (max_steps < (dest - start) / speed):
			max_steps = (dest - start) / speed
	
	outf.write("Case #" + str(i+1) + (": %06f" % (dest/max_steps)) + "\n")

