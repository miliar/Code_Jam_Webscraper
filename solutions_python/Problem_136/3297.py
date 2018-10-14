
__author__ = 'areksredzki'

def run_cookie():
	cf = open("cookie.io", "r")
	for x in range(0, int(cf.readline())):
		time = 0.0
		rate = 2.0
		data = cf.readline().strip().split()
		data = map(float, data)
		while data[2] != 0:
			if (data[2] < data[0]) or (data[2]/rate) <= (data[0]/rate + data[2]/(rate + data[1])):
				time += data[2]/rate
				data[2] = 0
			else:
				time += data[0]/rate
				rate += data[1]

		print "Case #" + str(x+1) + ": " + str(time)

	cf.close()


def run_magic():
	mf = open("magic.io", "r")
	for x in range(0, int(mf.readline())):
		data1 = []
		data2 = []
		data3 = []
		data1.append(mf.readline().strip())
		for i in range(1, 5):
			data1.append(mf.readline().strip().split())
		data2.append(mf.readline().strip())
		for i in range(1, 5):
			data2.append(mf.readline().strip().split())
		data3 = list(set(data1[int(data1[0])]).intersection(data2[int(data2[0])]))

		if len(data3) == 1:
			print "Case #" + str(x+1) + ": " + data3[0]
		elif len(data3) > 1:
			print "Case #" + str(x+1) + ": Bad magician!"
		else:
			print "Case #" + str(x+1) + ": Volunteer cheated!"

	mf.close()


if __name__ == '__main__':
	run_cookie()
