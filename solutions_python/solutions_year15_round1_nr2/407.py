# define gcd function
def gcd(x, y):
   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

if __name__ == '__main__':
	T = int(raw_input())

	for i in xrange(0, T):
		input_line = raw_input().split()
		B = int(input_line[0])
		position = int(input_line[1])
		barbers = map(lambda x: int(x), raw_input().split())

		if position <= B:
			print "Case #%d: %d" %(i+1, position)
		else:
			lcm_barbers = lcm(barbers[0], barbers[1])
			for barber in barbers[2:]:
				lcm_barbers = lcm(lcm_barbers, barber)

			time_split = []
			for barber in barbers:
				time_split.append(lcm_barbers/barber)

			#print time_split

			num_people = position % sum(time_split)
			if num_people == 0:
				num_people = sum(time_split)

			
			if num_people <= B:
				print "Case #%d: %d" %(i+1, num_people)
			else:
				num_people -= B
				attendent = -1
				j = 0
				solved = False
				while solved == False:
					j+=1
					for at, barber in enumerate(barbers):
						if (j % barber == 0):
							num_people -= 1
							if num_people == 0:
								attendent = at
								solved = True
								break

			
				print "Case #%d: %d" %(i+1, attendent+1)