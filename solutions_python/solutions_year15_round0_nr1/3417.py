def findGuests(inp):
	max_shyness = inp[0]
	shyness_array = inp[1:]

	guests = 0
	cumulated_ppl = 0


	for i in range(len(shyness_array)) :
		if i > cumulated_ppl :
			guests += i -cumulated_ppl
			cumulated_ppl = i
		cumulated_ppl += int(shyness_array[i])

	return guests


if __name__ == "__main__":

	with open("input") as f:
		f.readline()
		i = 1
		for line in f:
			shyness_array = line[1:len(line)-1]
			print("Case #"+str(i)+": "+str(findGuests(shyness_array)))
			i = i+1

	#res = findGuests(test)