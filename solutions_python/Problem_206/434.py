input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string

def formatted(x, y):
    return "Case #" + str(x) + ': ' + str(y) + '\n'

testcases = int(file_input())

for x in range(1, testcases + 1):
    distance, speed = file_input().split()
    distance = int(distance)
    horses = int(speed)

    
    y = 0.0

    
    for i in range(horses):
        a, b = file_input().split()
        a = float(a)
        b = float(b)
        time = (distance - a) / b
        if time > y:
            y = time
    
    y = distance/y
    output_file.write(formatted(x, y))
    
input_file.close()
output_file.close()
