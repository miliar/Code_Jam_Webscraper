import sys




def number(line):
    letters = {}
    numbers = []
    for char in line:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    if 'Z' in letters:
        while(letters['Z'] > 0):
            letters['Z'] -= 1
            letters['E'] -= 1
            letters['R'] -= 1
            letters['O'] -= 1
            numbers.append(0)
    if 'X' in letters:
        while(letters['X'] > 0):
            letters['S'] -= 1
            letters['I'] -= 1
            letters['X'] -= 1
            numbers.append(6)

    if 'U' in letters:
        while(letters['U'] > 0):
            letters['F'] -= 1
            letters['O'] -= 1
            letters['U'] -= 1
            letters['R'] -= 1
            numbers.append(4)
            
    if 'W' in letters:
        while(letters['W'] > 0):
            letters['T'] -= 1
            letters['W'] -= 1
            letters['O'] -= 1
            numbers.append(2)

    if 'G' in letters:
        while(letters['G'] > 0):
            letters['E'] -= 1
            letters['I'] -= 1
            letters['G'] -= 1
            letters['H'] -= 1
            letters['T'] -= 1
            numbers.append(8)

    if 'O' in letters:
        while(letters['O'] > 0):
            letters['O'] -= 1
            letters['N'] -= 1
            letters['E'] -= 1
            numbers.append(1)    

    if 'F' in letters:
        while(letters['F'] > 0):
            letters['F'] -= 1
            letters['I'] -= 1
            letters['V'] -= 1
            letters['E'] -= 1
            numbers.append(5)

    if 'V' in letters:
        while(letters['V'] > 0):
            letters['S'] -= 1
            letters['E'] -= 1
            letters['V'] -= 1
            letters['E'] -= 1
            letters['N'] -= 1
            numbers.append(7)

    if 'I' in letters:
        while(letters['I'] > 0):
            letters['N'] -= 1
            letters['I'] -= 1
            letters['N'] -= 1
            letters['E'] -= 1
            numbers.append(9)

    if 'T' in letters:
        while(letters['T'] > 0):
            letters['T'] -= 1
            letters['H'] -= 1
            letters['R'] -= 1
            letters['E'] -= 1
            letters['E'] -= 1
            numbers.append(3) 

    numbers.sort()
    answer = ""
    for elem in numbers:
        answer += str(elem)
    return answer

in_file = open("A-large.in", 'r')
out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip()
    sol = number(line)

    answer = "Case #" + str(case) + ": " + sol + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

