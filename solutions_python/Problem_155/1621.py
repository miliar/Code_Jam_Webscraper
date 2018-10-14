i = open("A-large.in", 'r')
o = open('out.txt', 'w')

num_case = i.readline()
num_case = int(num_case)

for case in range(1, num_case + 1):
    case = str(case)
    line = i.readline()
    line = line.split()
    audience = line[1]
    list_of_digits = []
    for each in audience:
        each = int(each)
        list_of_digits.append(each)
    min_num = 0
    for member in range(len(list_of_digits) - 1):
        if list_of_digits[member] == 0:
            if member == 0:
                min_num += 1
                list_of_digits[0] = 1
            else:
                count = 0
                counter = 1
                while member - counter >= 0:
                    count += list_of_digits[member - counter]
                    counter += 1
                counter2 = 0
                while list_of_digits[member + counter2] == 0:
                    counter2 += 1
                if count >= member + counter2:
                    pass
                else:
                    min_num += 1
                    list_of_digits[member] = 1
    o.write("Case #" + case + ": " + str(min_num) + "\n")

o.close()
