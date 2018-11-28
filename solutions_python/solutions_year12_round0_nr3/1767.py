#Program : Recycled Number, Google code jam problem C
#Author  : Santhosh Unnikrishnan
#email   : santa001@gmail.com
#date    : 14th April 2012

IN_FILE_NAME   = "C-small-attempt.in"
OUT_FILE_NAME  = "C-small-attempt.out"
TEMP_FILE_NAME = "temp.txt"

def get_number_of_recycled_numbers(A, B):
	''' This function will return the number of recyclable number in [A,B]
	'''
	count = 0

	n = A
	fd = open(TEMP_FILE_NAME, "w")

	while n <= B:
		num = len(str(n))
		i = 1
		while i <= num-1:
			number = n % (10 ** i)
			if number == 0:
				i = i + 1
			else:
				#print n, number
				m = (number * (10 ** (num-i))) + (n/(10 ** i))
				#print "m is %d" %(m)
				if m > n and m <= B:
					count = count + 1
					string = "%d-%d\n" %(n, m)
					fd.write(string)
				i = i + 1
		n = n + 1
	fd.close()
	
	print 'Original count %d' %(count)

	fd = open(TEMP_FILE_NAME, "r")
	contents = fd.readlines()

	i = 0
	j = 0
	
	new_count = count
	while i < count:
		j = i + 1
		while j < count:
			if contents[i] == contents[j]:
				new_count = new_count - 1
			j = j + 1
		i = i + 1

	fd.close()
	return new_count

if __name__ == "__main__":
	fd = open(IN_FILE_NAME, "r")
	contents = fd.readlines()
	fd.close()

	test_cases = int (contents[0])
	count = 0
	mylist = []
	number = 0

	fd = open(OUT_FILE_NAME, "w")

	while count < test_cases:
		string = contents[count + 1]
		mylist = string.split(" ")
		if len(mylist) < 2:
			number = 0
		else :
			A = int(mylist[0])
			B = int(mylist[1])
		
			number = get_number_of_recycled_numbers(A,B)
		count = count + 1
		out_put_string = "Case #%d: %d\n" %(count, number)
		fd.write(out_put_string)

	fd.close()
