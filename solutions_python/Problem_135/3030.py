import math

def difference(first, second):
	setfinalone = set()
	for number in first.split(" "):
		setfinalone.add(number)

	setfinaltwo = set()
	for number in second.split(" "):
		setfinaltwo.add(number)

	diff = setfinalone & setfinaltwo
	if len(diff) > 1:
		return "Bad magician!"
	elif len(diff) < 1:
		return "Volunteer cheated!"
	else:
		return str(diff.pop())

def main():
	f = open('/Users/alex/Downloads/A-small-attempt1.in.txt')
	nTests = int(f.readline().replace("\n",""))

	for i in range(nTests):
		set1 = None
		set2 = None
		first_answer = int(f.readline().replace("\n",""))
		for j in range(4):
			if j+1 == first_answer:
				set1 = f.readline().replace("\n","")
			else:
				f.readline()
		second_answer = int(f.readline().replace("\n",""))
		for j in range(4):
			if j+1 == second_answer:
				set2 = f.readline().replace("\n","")
			else:
				f.readline()

		print "Case #" + str(i+1) + ": " + difference(set1, set2)


if __name__ == "__main__":
    main()
