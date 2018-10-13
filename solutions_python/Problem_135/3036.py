#-*-coding:utf-8-*-


if __name__ == "__main__":
    data_file_path = "A-small-attempt0.in"

    test_num = None

    dict = {}
    with open(data_file_path) as file:
        lines = file.readlines()
        first_line = lines[0].strip()
        test_num = int(first_line)

        answer = None
        for test_index in xrange(0, test_num):
            answer1 = None
            array1 = []
            answer2 = None
            array2 = []
            test = dict.get(test_index, {})

            # print 1 + test_index * 10
            # print (test_index + 1) * 10 + 1
            # print "---------"

            for line in lines[1 + test_index * 10:(test_index + 1) * 10 + 1]:
                line = line.strip()
                if answer1 == None:
                    answer1 = line
                    continue

                if len(array1) < 16:
                    nums = line.split(" ")
                    array1.extend(nums)
                    continue

                if answer2 == None:
                    answer2 = line
                    continue

                if len(array2) < 16:
                    nums = line.split(" ")
                    array2.extend(nums)

            test[1] = [answer1, array1]
            test[2] = [answer2, array2]

            dict[test_index] = test

    # print test_num
    # print dict


    output_path = "test1_output0.txt"
    with open(output_path, "w") as output_file:
        for test_index in xrange(test_num):
            test = dict[test_index]
            answer1 = int(test[1][0]) - 1
            array1 = test[1][1]
            answer2 = int(test[2][0]) - 1
            array2 = test[2][1]

            row1 = array1[answer1 * 4:(answer1+1) * 4]
            row2 = array2[answer2 * 4:(answer2+1) * 4]

            intersection = set(row1).intersection(set(row2))
            possible_choice_num = len(set(row1).intersection(set(row2)))

            if possible_choice_num == 0:
                output_file.write("Case #" + str(test_index + 1) + ": Volunteer cheated!\n")

            if possible_choice_num == 1:
                output_file.write("Case #" + str(test_index + 1) + ": " + str(list(intersection)[0]) + "\n")

            if possible_choice_num > 1:
                output_file.write("Case #" + str(test_index + 1) + ": Bad magician!\n")






