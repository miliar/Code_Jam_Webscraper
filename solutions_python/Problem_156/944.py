def eat(dishes):
	return [(i-1 if i > 0 else 0) for i in dishes]


def eaten(dishes):
	return max(dishes) == 0


def special(dishes):
	largest = max(dishes)
	sharer = dishes.index(largest)
	
	# split dish
	part = int(largest/2) if largest != 9 else 6
	part2 = largest - part
	dishes[sharer] = part
	
	dishes.append(part2)
	return dishes


def opt(dishes):
	if (eaten(dishes)): return 0

	if (max(dishes) <= 2): return opt(eat(dishes))+1
	# print "####"
	return min(opt(eat(dishes))+1, opt(special(dishes))+1)
	# return opt(eat(dishes))+1



infile = open("test", 'r') # open file for appending
outfile = open("result2","w") # open file for writing

firstLine = infile.readline()
case = 0

while True:
    diners = infile.readline()
    dishes = infile.readline()

    if not diners or not dishes: 
    	break

    dishes = [int(i) for i in dishes.rstrip("\n").split(" ")]


    minutes = opt(dishes) 
    case += 1
    output = "Case #"+str(case)+": "+str(minutes)
    outfile.write(output+"\n")
    print output


infile.close()
outfile.close()