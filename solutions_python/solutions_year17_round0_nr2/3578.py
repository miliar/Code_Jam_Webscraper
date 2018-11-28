def get_split(number):
    num_list = []
    while number > 0:
        num_list.append(number % 10)
        number = number / 10
    num_list.reverse()
    return num_list

def is_tidy(number):
    ln = len(number)
    for i in range(ln - 1):
        if number[i] > number[i + 1]:
            return False
    return True

def last_tidy_num(number):
    if number < 10:
        return number
    sp_number = get_split(number)
    ln = len(sp_number)
    i,j = ln - 1, ln - 2
    while not is_tidy(sp_number):
        sp_number[i] = 9
        sp_number[j] = sp_number[j] - 1
        i = j
        j = j - 1
    return unite_number(sp_number)

def unite_number(sp_number):
    number = 0
    for i in sp_number:
        number = number * 10
        number = number + i
    return number
"""
def last_tidy_num(number):
    if is_tidy(number):
        return number
    else:
        return last_tidy_num(number - ((number % 10) + 1))
"""
#main
t = int(raw_input())
for i in range(t):
    number = int(raw_input())
    x = last_tidy_num(number)
    string_print = "Case #" + str(i + 1) + ": " + str(x)
    print string_print
