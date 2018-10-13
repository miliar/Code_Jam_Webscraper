i = open('A-large.in', 'r') 
o = open('largeout.txt', 'w') 

num = i.readline() 
num = int(num) 

for x in range(1, num + 1): 
    x = str(x)
    num2 = i.readline()
    num2 = num2.split()
    audience = num2[1]
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
    o.write("Case #" + x + ": " + str(min_num) + "\n")