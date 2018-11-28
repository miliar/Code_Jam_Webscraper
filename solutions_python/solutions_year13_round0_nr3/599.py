import sys, math

number = 1
MAXIMUM = math.pow(10, 14)
square = 1
ARRAY = []
length = 0
while square < MAXIMUM:
    string_number = str(number)
    if all(string_number[i] == string_number[-(i + 1)]
        for i in range(len(string_number) / 2)):
	string_square = str(square)
	if all(string_square[i] == string_square[-(i + 1)]
	    for i in range(len(string_square) / 2)):
	    ARRAY.append(square)
	    length += 1
    number += 1
    square = number * number

line = sys.stdin.readline()
NUMBER = int(line.strip())

for case in range(0, NUMBER):
    line = sys.stdin.readline().strip().split()
    low = int(line[0])
    high = int(line[1])
    start = 0
    while start < length:
        if ARRAY[start] >= low:
            break
        start += 1
    end = length - 1
    while end >= 0:
        if ARRAY[end] <= high:
            break
        end -= 1
    output = end - start + 1
    output = output if output > 0 else 0
    print 'Case #%d: %s' % (case + 1, output)
