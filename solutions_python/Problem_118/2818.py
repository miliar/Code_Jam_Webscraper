import math

def is_palindrom(x):
	y = x[::-1]
	if x==y:
		return True
	else:
		return False

start = 1
end = 4

def num_palindromes(start, end):
    count = 0
    for i in range(start, end + 1):
    	print i
        if str(i) == str(i)[::-1]:
            num = i**(1/2)
            print "%d \n" %num 
            if is_palindrom(str(num)):
            	count += 1

    return count

if __name__ == "__main__":
	print "\nTotal Count is %d" %num_palindromes(start, end)


	
pands = []

def generate_pands():
    cur = 1
    for i in xrange(1000000):
        poss = cur * cur
        if is_palindrome(poss):
            pands.append(poss)
        cur = find_next_palindrome(cur)

def method_2(lower,upper):
    count = 0
    for x in pands:
        if x >= lower and x <= upper:
            count += 1
    return count