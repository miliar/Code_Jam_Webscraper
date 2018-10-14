
file_input = open("tidy-large.in","r") 
file = open("tidy-large.out", "w+") 

num_cases = int(file_input.readline().rstrip())

def new_number(number):
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i] -= 1

            for change in range(i + 1, len(number)):
                number[change] = 9

            if i == 0 and number[i] == 0:
                number.pop(0)

            return new_number(number)

    return number


for case in range(num_cases):
    line = file_input.readline().rstrip()
    
    number = line
    number = list(number)
    number = [int(digit) for digit in number]

    new_num = new_number(number)
    new_num = [str(num) for num in number]

    new_num = int("".join(new_num))

    file.write("Case #" + str(case + 1) + ": " + str(new_num) + "\n")

file_input.close()
file.close()