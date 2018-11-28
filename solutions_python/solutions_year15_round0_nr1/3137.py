def main():
	f = open("in.txt")
	n = int(f.readline())
	for x in xrange(1, n+1):
		line = f.readline()
		number_of_levels = int(line.split(" ")[0])
		shyness = map(int,list(line.split(" ")[1].strip()))
		number_of_people_to_add = 0
		number_of_people_standing = 0
		if number_of_levels != 0:
			number_of_people_standing = shyness[0]
			for shyness_level in xrange(1, number_of_levels + 1):
				if number_of_people_standing < shyness_level:
					number_of_people_to_add += shyness_level - number_of_people_standing
					number_of_people_standing = shyness_level
				number_of_people_standing += shyness[shyness_level]
		print "Case #%d:  %d" % (x, number_of_people_to_add)
	

if __name__ == '__main__':
	main()