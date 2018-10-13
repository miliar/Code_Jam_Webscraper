input_file_path = "A-small-attempt0.in"
input_data = open(input_file_path).read().splitlines()
outputFilePath = open("output.txt", "w")

num_cases = int(input_data[0].strip())

# for each case
for case_index in range(0, num_cases):

    case = input_data[case_index + 1].split(' ')
    seated_people_length = int(case[0]) + 1
    seated_people = list(map(int, case[1]))
    friend_count = 0

    # for each seated_people_string in case
    for seated_people_STRING_index in range(0, seated_people_length):

        if seated_people_STRING_index == 0:
            continue

        # for each class of person with a particular shyness
        for shyness_index in range(1, seated_people_length):

            total_standing = 0

            # for each person that came before this particular shyness index category
            for previous_shyness_index_people in range(0, shyness_index):
                total_standing += seated_people[previous_shyness_index_people]

            while shyness_index > total_standing:
                friend_count += 1
                total_standing += 1
                seated_people[shyness_index - 1] += 1


    output_line = "Case #%s: %d\n" % (case_index + 1, friend_count)
    outputFilePath.write(output_line)

outputFilePath.close()