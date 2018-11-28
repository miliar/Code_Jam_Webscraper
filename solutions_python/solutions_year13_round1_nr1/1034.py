from decimal import *

import math
f = open("/Users/mklein16/Desktop/jam/A-small-attempt0.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")
for i in range(cases):
	numbers = contents[i+1]
	numbers = numbers.split(" ")
	r = Decimal(numbers[0])
	t = Decimal(numbers[1])
	a = 2.0
	b = Decimal(2*r-1)

	middle = Decimal((b**2)+(8*t))
	middle = Decimal(math.sqrt(Decimal(middle)))
	answer2 = Decimal(Decimal(Decimal(-b)+Decimal(middle))/(4))

	answer = int(answer2)



	if answer > answer2:
		answer -= 1



	g = open("/Users/mklein16/Desktop/jam/output.txt", 'a')
	g.write("Case #" + `i+1`+": " + str(answer) + "\n")
	g.close()






