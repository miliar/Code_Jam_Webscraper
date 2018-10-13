class Robot():
	def __init__(self, name, orders):
		self.orders = orders
		self.position = 1
		self.name = name

	def act(self, current, lock): # takes the list of overall orders and a "lock"
		#Counting the possibilities off to myself.
		if len(self.orders) is 0:
			print "%s is done." % self.name

		elif self.position == self.orders[0] == current[0][1]:
			if self.name.startswith(current[0][0]) and not lock["lock"]:
				print "%s pressing button at %s." % (self.name, self.orders[0])
				self.orders.pop(0)
				current.pop(0)
				lock["lock"] = True
			else: print "%s waiting for other guy to get THUMB OUT OF ASS"

		elif self.position == self.orders[0]:
			print "%s waiting at %s" % (self.name, self.position)

		else:
			self.move()

	def move(self):
		if self.position > self.orders[0]:
			self.position -= 1
		elif self.position < self.orders[0]:
			self.position += 1
		print "%s moved to %s." % (self.name, self.position)

def loop(line):
	(o,b,a) = parse_orders(line)

	orange = Robot("Orange",o)
	blue = Robot("Blue",b)

	lock = {"lock": False}
	seconds = 0
	while(len(orange.orders) or len(blue.orders)):

		blue.act(a, lock)
		orange.act(a, lock)
		seconds += 1
		lock["lock"] = False

		print "Blue's remaining orders: %s" % blue.orders
		print "Orange's reminaing orders: %s" % orange.orders

		print "%s seconds." % seconds
		print "%s remaining orders." % a 
	
	print "orange: %s, blue: %s" % (orange.orders, blue.orders)
	print seconds
	return seconds

def parse_orders(line):
	splitted = line.split()[1:]
	pairs = []
	for i in range(0, len(splitted), 2):
		pair = (splitted[i], splitted[i+1])
		pairs.append(pair)

	a = map(lambda x: (x[0], int(x[1])), pairs)

	o = filter(lambda x: x[0] == "O", pairs)
	o = map(lambda x: int(x[1]), o)

	b = filter(lambda x: x[0] == "B", pairs)
	b = map(lambda x: int(x[1]), b)

	return (o,b,a)
	



def main():
	with open("A-large.in", "r") as input_file:
		with open("test.out", "w") as output_file:
			index = 0
			for line in input_file:
				if len(line.split()) == 1:
					continue
				
				index += 1
				
				result = "Case #{0}: {1}\n".format(index, loop(line))
				output_file.write(result)

if __name__ == '__main__':
	main()