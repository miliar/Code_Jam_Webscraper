
def check_10(number):
    sequence = str(number)
    zero_started = False
    for num in sequence:
        num = int(num)
        if num > 1:
            return False

        if zero_started and num == 1:
            return False

        if num == 0:
            zero_started = True

    return True

def check_tidy(number):
    sequence = str(number)
    tidy = False
    prev_num = 0
    for num in sequence:

        num = int(num)
        if num >= prev_num:
            tidy = True
        else:
            tidy = False
            return tidy
        prev_num = num

    return tidy

def find_tidy(last_number):
    if last_number == 1:
        return '1'
    if check_10(last_number):
        return '9' * (len(str(last_number)) -1)

    if check_tidy(last_number):
        return last_number

    for i in range(last_number, 0, -1):
        if check_tidy(i):
            return i

    return 0

output = open('output.txt', 'w')

with open("B-small-attempt2.in", "r") as file:
    count = 0
    for line in file:
        count += 1
        if count == 1:
            cases = int(line)
        else:
            last_number = int(line)
            output.write("Case #"+str(count-1)+": " + str(find_tidy(last_number))+"\n")