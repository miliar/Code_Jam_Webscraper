def number_to_list(number):
    string = str(number)
    digit_list = []
    for digit in string:
        digit_list.append(int(digit))
    return digit_list

def list_to_number(list):
    return int(''.join(map(str, list)))

def is_tidy(number):
    digits = number_to_list(number)
    for i in range(len(digits) - 1):
        current_digit = digits[i]
        next_digit = digits[i + 1]
        if current_digit > next_digit:
            return False
    return True


def tidy_the_number(number):
    digits = number_to_list(number)
    #Go through the digits backwards
    for i in range(len(digits)-1, -1, -1):
        if i == 0:
            return list_to_number(digits)
        #We need to do some tidying if the previous number is bigger...
        if digits[i] < digits[i - 1]:
            #Take 1 of the next number up...
            digits[i - 1] = digits[i - 1] - 1
            #Convert everything that is the current number and lower to a 9
            for j in range(i, len(digits)):
                digits[j] = 9            

input_file = open("b_large_input.txt", "r")
output_file = open("b_large_output.txt", "w")
data = input_file.readlines()
T = int(data[0])
for t in range(1, T+1):
    N = int(data[t])
    tidy = tidy_the_number(N)
    output_file.write("Case #{}: {}\n".format(t, tidy))

input_file.close()
output_file.close()
print("Files closed")
