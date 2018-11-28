#!/usr/bin/python

def get_file_contents():
    input_file = "input.txt"
    file = open(input_file, "r")
    return file

def get_number_of_test_cases(file):
    test_cases_string = file.readline()
    test_cases_integer = int(test_cases_string)
    return test_cases_integer

def print_results(answers):
    i = 1
    while i <= len(answers):
        print "Case #" + str(i) + ": " + str(answers[i-1])
        i += 1

def get_data_from_input_file(file):
    data = []
    for line in file:
        row = []
        line = remove_new_line(line)
        split_line = split_max_shyness_level_from_audience(line)
        max_shyness_level = int(split_line[0])
        audience = convert_audience_to_array(split_line[1])
        row.append(max_shyness_level)
        row.append(audience)
        data.append(row)
    return data

def convert_audience_to_array(audience_string):
    return map(int, audience_string)

def remove_new_line(line):
    return line.rstrip("\n")

def split_max_shyness_level_from_audience(line):
    return line.split(" ")

def get_answers(input_data):
    answers = []
    for row in input_data:
        max_shyness_level = row[0]
        audience = row[1]
        added_friends = 0
        number_of_people_standing_up = 0
        current_shyness_level = 0
        while current_shyness_level <= max_shyness_level:
            number_of_people_standing_up += audience[current_shyness_level]
            if number_of_people_standing_up <= current_shyness_level:
                added_friends += 1
                number_of_people_standing_up += 1
            current_shyness_level += 1
        answers.append(added_friends)
    return answers


def main():
    file = get_file_contents()
    number_of_test_cases = get_number_of_test_cases(file)
    input_data = get_data_from_input_file(file)
    answers = get_answers(input_data)
    print_results(answers)

main()
