class FileWrapper:
    def __init__(self, file):
        self.file = file
    
    def getInt(self):
        return int(self.file.readline())
    
    def getInts(self):
        return [int(z) for z in self.file.readline().split()]
    
    def getFloat(self):
        return float(self.file.readline())
    
    def getFloats(self):
        return [float(z) for z in self.file.readline().split()]
    
    def getWords(self):
        return self.file.readline().split()
    
    def readline(self):
        return self.file.readline().strip()
    
    def close(self):
        self.file.close



fo = open("B-large.in", "r+")
fw = FileWrapper(fo)


num_test_cases = fw.getInt()

for x in xrange(0, num_test_cases):

	values = fw.getFloats()

	farm_price = values[0]
	farm_per_second = values[1]
	cookies_needed = values[2]

	cookie_count = 0.0
	farm_count = 0.0
	seconds_elapsed = 0.0

	base_per_second = 2.0

	while cookie_count < cookies_needed:
		current_per_second = base_per_second + farm_count * farm_per_second
		seconds_until_farm = farm_price / current_per_second

		if (current_per_second * seconds_until_farm) >= (cookies_needed - cookie_count):
			seconds_elapsed += (cookies_needed - cookie_count)/current_per_second
			cookie_count = cookies_needed
			break

		seconds_elapsed += seconds_until_farm
		cookie_count += current_per_second * seconds_until_farm

		#time to complete on current track
		seconds_left = (cookies_needed - cookie_count) / current_per_second

		#time to complete if purchase farm
		cookies_remaining_with_farm = cookies_needed - (cookie_count - farm_price)
		with_farm_per_second = current_per_second + farm_per_second
		farm_seconds_left = cookies_remaining_with_farm / with_farm_per_second

		if farm_seconds_left < seconds_left:
			cookie_count -= farm_price
			farm_count += 1

	
	print "Case #" + str(x+1) + ": " + str(seconds_elapsed)


fw.close()
