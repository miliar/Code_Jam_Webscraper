def is_tidy(string):
    for idx, x in enumerate(string):
        if idx + 1 < len(string) and x > string[idx + 1]:
            return False
    return True

def transform(number):
    cambios = False
    new_number = ''
    for idx, y in enumerate(number):
        if not cambios:
            new_number = new_number + y
        else:
            new_number = new_number + '0'
        if not cambios and idx+1 < len(number) and y > number[idx+1]:
            cambios = True
    if len(new_number) != 1:
        numero = int(new_number) - 1
        new_number = str(numero)
    return new_number

def solve(number):
    while not is_tidy(number):
        number = transform(number)
    return number

file = open('B-large.in')
output = open('answer-long.txt','w')
cases = int(file.readline())  # read a line with a single integer
for i in range(1, cases + 1):
    number = file.readline().strip()
    output.write('Case #'+str(i)+': '+solve(number)+'\n')
output.close()