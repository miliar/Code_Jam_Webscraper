#Google Code Jam PANCAKE FLIPPER

no_lines_str = input()
no_lines = int(no_lines_str)

count = no_lines

input_list = []

while count > 0:
    test_list = []
    test_num_str = input()
    test_list = test_num_str.split(" ")
    input_list.append(test_list)

    count -= 1
count_int = 1
for i in input_list:
    count = 0
    list_try = i
    flips_str = list_try[-1]
    flips = int(flips_str)
    i_temp = []
    for abc in list_try[0]:
        i_temp.append(abc)
    len_list = len(i_temp)

    for j in range(0, (len_list - flips + 1)):
        j_temp = i_temp[j]
        if j_temp == "-":
            count += 1
            j_spot = i_temp.index(j_temp)
            for k in range(j_spot,(j_spot + flips)):
                if i_temp[k] == "-":
                    i_temp[k] = "+"
                elif i_temp[k] == "+":
                    i_temp[k] = "-"

    check = 0
    for x in i_temp:
        if x == "+":
            check += 0
        elif x == "-":
            check += 1
    
    if check == 0:
        print("Case #%i: " % count_int + str(count))
        count_int += 1
    else:
        print("Case #%i: IMPOSSIBLE" % count_int)
        count_int += 1
