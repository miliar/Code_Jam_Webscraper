input_file = open('B-small-attempt4.in')

t = int(input_file.next().rstrip('\n'))  # The first line of the input gives the number of test cases, T.

test_cases = []
for x in range(t):  # T test cases follow.
    start_num_plates = int(input_file.next().rstrip('\n'))  # Each consists of one line with D, the number of diners with non-empty plates,

    plates = input_file.next().rstrip('\n').split(" ")  # D space-separated integers representing the numbers of pancakes on those diners' plates.
    for y in xrange(len(plates)):
        plates[y] = int(plates[y])

    #not_worth_splitting_list = []

    def recursive_split(input_plates, time_so_far):
        if sum(input_plates) == 0:
            return 0

        max_plate = max(input_plates)

        # if max pancake count is 1, then no need to try to split (this is last round)
        if max_plate == 1:
            return time_so_far + 1

        # Case One: let run out
        best_option = time_so_far + max_plate

        input_plates.remove(max_plate)

        # Case Two: split tallest plate
        for pancakes_on_the_move in xrange(1, max_plate//2 + 1):
            #if pancakes_on_the_move in not_worth_splitting_list:
            #    continue

            test_input_plates = list(input_plates)
            test_input_plates.append(pancakes_on_the_move)
            test_input_plates.append(max_plate-pancakes_on_the_move)
            result = recursive_split(test_input_plates, time_so_far + 1)
            if result < best_option:
                best_option = result
            elif result == best_option:
                continue
            elif result > best_option:
                break

        return best_option

    print('Case #'+str(x+1)+': ' + str(recursive_split(plates, 0)))