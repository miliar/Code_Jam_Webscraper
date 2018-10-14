from sys import argv
from math import sqrt

def is_palindrome(number):
    number = list(str(number))
    i = 0
    j = len(number)-1
    while i<j:
        if number[i] != number[j]:
            return False
        i = i+1
        j = j-1
    return True

pals = [0, 1, 4, 9, 121, 484, 676, 10201, 12321, 14641, 40804, 44944, 69696, 94249, 698896, 1002001, 1234321, 4008004, 5221225, 6948496, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 522808225]   

def findanswer(line, j):
    numbers = []
    solution = []
    square = 0
    line = list(line.split())
    for word in line:
        word = float(word)
        numbers.append(word)
    for pal in pals:
        if numbers[0] <= pal <= numbers[1] and is_palindrome(int(sqrt(pal))):
            solution.append(pal)
    answer = len(solution)
    print "Case #%d: %s" % (j, answer)    
    
     
with open(argv[1]) as f:
	T = eval(f.readline())
	j = 0
	for line in f:
	    j += 1
	    findanswer(line, j)
