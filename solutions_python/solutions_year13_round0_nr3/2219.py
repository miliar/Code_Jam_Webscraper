import math
input_file = open('attempt.txt', 'r')
text = input_file.read().split()
cases = int(text[0])
text = text[1:]

ranges = []
for i in range(cases):
    ranges.append(text[2*i: 2*i + 2])
 
def palindrome(word):
    i = 0
    word = str(word)
    while i <= len(word) / 2:
        if word[i] != word[len(word) - 1 - i]:
            return False
        i += 1
    return True

def populate_sq(lower, upper):
    squares = []
    count = 3
    curr = 1
    while curr <= upper:
        if curr >= lower:
            squares.append(curr)
        curr += count
        count += 2
    return squares

def find_fairsquare(ranges):
    i = 0
    affirmed = []
    for _ in range(cases):
        affirmed.append([])
    for case in ranges:
        squares = populate_sq(int(case[0]), int(case[1]))
        
        for num in squares:
            if palindrome(num):
                if palindrome(int(num**.5)):
                    affirmed[i].append(num)
        i += 1
    return affirmed

fairsquare_nums = find_fairsquare(ranges)
outputs = []
for i in fairsquare_nums:
    outputs.append(len(i))
         
def format_out(outputs):
    i = 1
    for item in outputs:
        print('Case #' + str(i) + ': ' + str(item))
        i += 1 
        
format_out(outputs)  
