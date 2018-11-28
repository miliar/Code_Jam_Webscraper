import sys

def read_test_cases(input_file_name):
    test_cases = []

    f = open(input_file_name)

    T = int(f.readline())

    for i in xrange(T):
        raw_test_case = f.readline()
        splitted = raw_test_case[:-1].split(" ")[1:]
        test_case = zip(splitted[::2], map(int, splitted[1::2]))
        test_cases.append(test_case)
    
    f.close()

    return test_cases

def get_seconds(test_case):
    seconds = 0
    orange_can_move = True
    blue_can_move = True
    orange_position = 1
    blue_position = 1

    while len(test_case) > 0:
        seconds += 1

        current_goal = test_case[0]

        blue_goals = filter(lambda x: x[0] == "B", test_case)
        current_blue_goal = blue_goals[0] if len(blue_goals) > 0 else None

        orange_goals = filter(lambda x: x[0] == "O", test_case)
        current_orange_goal = orange_goals[0] if len(orange_goals) > 0 else None

        blue_can_move = current_blue_goal is not None and \
                        (blue_position != current_blue_goal[1])

        orange_can_move = current_orange_goal is not None and \
                        (orange_position != current_orange_goal[1])
   
        blue_can_press = (current_blue_goal == current_goal) and \
                         (blue_position == current_blue_goal[1])

        orange_can_press = (current_orange_goal == current_goal) and \
                         (orange_position == current_orange_goal[1])

        if blue_can_move:
            if blue_position < current_blue_goal[1]:
                blue_position += 1
            else:
                blue_position -= 1

        if orange_can_move:
            if orange_position < current_orange_goal[1]:
                orange_position +=1
            else:
                orange_position -= 1

        if blue_can_press or orange_can_press:
            test_case.pop(0)

    return seconds

def write_results(output_file_name, results):
    f = open(output_file_name, 'wt')

    for i, result in enumerate(results):
        f.write("Case #%d: %d\n" % (i + 1, result))

    f.close()

def main():
    assert len(sys.argv) == 3

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    test_cases = read_test_cases(input_file_name)

    results = []

    for test_case in test_cases:
        seconds = get_seconds(test_case)
        results.append(seconds)

    write_results(output_file_name, results)
        

if __name__ == "__main__":
    main()
