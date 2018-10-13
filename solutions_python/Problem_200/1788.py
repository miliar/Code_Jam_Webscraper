cases_number = int(raw_input())
test_cases = []
for i in range(cases_number):
    test_cases.append(raw_input())

def is_tidy(num_array):
    for index in range(len(num_array)-1):
        if num_array[index] > num_array[index+1]:
            return False
    return True


for i in range(cases_number):
    case = list(test_cases[i])
    for temp_index in range(len(case)):
        case[temp_index] = int(case[temp_index])

    clean = 0
    while clean < len(case)-1:
        if case[clean] > case[clean + 1]:
            break
        clean += 1

    right_most = len(case)-1

    while not is_tidy(case):
        case[right_most-1] = case[right_most-1]-1
        case[right_most] = 9
        right_most -= 1

    total = 0
    for digit in case:
        total *= 10
        total += digit
    print "Case #" + str(i+1) + ": " + str(total)
