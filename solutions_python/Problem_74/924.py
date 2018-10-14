def work_out_time(orange_order, blue_order, button_order):
    time = 0
    orange_place = 1
    blue_place = 1
    while not button_order == []:
        orange_push = False

        # Check if orange is at place
        if not orange_order == []:
            if not orange_place == orange_order[0]:
                if orange_place < orange_order[0]:
                    orange_place += 1
                else:
                    orange_place -= 1
            else:
                # Check if orange can press button
                if button_order[0] == 'O':
                    orange_push = True
                    button_order = button_order[1:]
                    orange_order = orange_order[1:]

        # Check if blue is at place
        if not blue_order == []:
            if not blue_place == blue_order[0]:
                if blue_place < blue_order[0]:
                    blue_place += 1
                else:
                    blue_place -= 1
            else:
                # Check if blue can press button
                if not orange_push:
                    if button_order[0] == 'B':
                        button_order = button_order[1:]
                        blue_order = blue_order[1:]
        time += 1
    return time

def create_input(test_case):
    test_split = test_case.split(" ")
    test_split = test_split[1:]
    button_order = []
    orange_order = []
    blue_order = []
    for command in range(len(test_split)):
        if not test_split[command].isdigit():
            button_order.append(test_split[command])
        else:
            if test_split[command - 1] == 'O':
                orange_order.append(int(test_split[command]))
            else:
                blue_order.append(int(test_split[command]))
    time = work_out_time(orange_order, blue_order, button_order)
    return time

in_file = open("in")
out_file = open("out", "w")
number_of_tests = int(in_file.readline())
for test in range(number_of_tests):
    test_line = in_file.readline()
    test_line = test_line[:-1]
    time = create_input(test_line)
    out_file.write("Case #" + str(test + 1) + ": " + str(time) + "\n")
out_file.close()
in_file.close()
