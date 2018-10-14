
import re

def read_input_file():
    input_file = open("./A-large.in")
    line_text = input_file.readline()
    match_object = re.match("^(\d+)$", line_text)
    if match_object is not None:
        match_text = match_object.group(0)
        number_of_test_cases = int(match_text)
        print("Number of test cases:", number_of_test_cases)

    pancake_text_list = []
    pancake_flip_size_list = []

    for x in range(number_of_test_cases):
        line_text = input_file.readline()
        match_object = re.match("^(.+)\s(\d+)$", line_text)
        if match_object is not None:
            pancake_text = match_object.group(1)
            pancake_flip_size_text = match_object.group(2)
            pancake_flip_size = int(pancake_flip_size_text)

        print("Pancake Text:", pancake_text)
        print("Pancake Flip Size:", pancake_flip_size)

        pancake_text_list.append(pancake_text)
        pancake_flip_size_list.append(pancake_flip_size)

    input_file.close()

    return number_of_test_cases, pancake_text_list, pancake_flip_size_list

def convert_pancake_text_to_integer(pancake_text):
    pancake_integer = 0
    number_of_pancakes = len(pancake_text)
    for x in range(number_of_pancakes):
        if pancake_text[number_of_pancakes-(x+1)] == "+":
            pancake_integer += 1<<x

    return pancake_integer

def flip_pancakes_with_flipper(start_index, flipper_size, pancake_integer, number_of_pancakes, flipper_integer):
    print("Binary flipper:", ("{0:0" + str(flipper_size) + "b}").format(flipper_integer))
    pancake_integer = pancake_integer^(flipper_integer<<(number_of_pancakes-flipper_size-start_index))

    return pancake_integer

def flip_pancakes_to_happy_side(pancake_text, pancake_flip_size):
    number_of_pancakes = len(pancake_text)

    flipper_integer = 0
    for x in range(pancake_flip_size):
        flipper_integer += 1 << x

    print("")
    print("Flipping:", pancake_text, number_of_pancakes)
    pancake_integer = convert_pancake_text_to_integer(pancake_text)
    flips_required = 0
    all_pancakes_smiling = False

    impossible_smile_flip = False

    print("Pancake integer:", pancake_integer)
    first_blank_pancake = -2
    while first_blank_pancake != -1 and not impossible_smile_flip and flips_required<1000:
        first_blank_pancake = -1
        for x in range(number_of_pancakes):
            if pancake_integer&1<<(number_of_pancakes-(x+1)) == 0:
                first_blank_pancake = x
                print("")
                print("First blank pancake:", first_blank_pancake)

                if (number_of_pancakes - first_blank_pancake < pancake_flip_size):
                    impossible_smile_flip = True
                    break

                print("Pancake text before flip:", ("{0:0" + str(number_of_pancakes) + "b}").format(pancake_integer))
                pancake_integer = flip_pancakes_with_flipper(first_blank_pancake, pancake_flip_size, pancake_integer, number_of_pancakes, flipper_integer)
                flips_required += 1
                print("Pancake text after flip:", ("{0:0"+str(number_of_pancakes)+"b}").format(pancake_integer))
                print("Flips made:", flips_required)
                break

    if first_blank_pancake == -1:
        all_pancakes_smiling = True
    print("Flips required:", flips_required)
    return flips_required, all_pancakes_smiling

def output_results_to_file(flips_required_list, all_pancakes_smiling_list):
    output_file = open("output_large.txt","w")
    for x in range(len(all_pancakes_smiling_list)):
        write_text = ""
        if all_pancakes_smiling_list[x]:
            write_text = "Case #"+str(x+1)+": "+str(flips_required_list[x])+"\n"
        else:
            write_text = "Case #"+str(x+1)+": IMPOSSIBLE\n"
        output_file.write(write_text)

    output_file.close()


def flip_pancake_cases_to_happy_side():
    number_of_test_cases, pancake_text_list, pancake_flip_size_list = read_input_file()

    flips_required_list = []
    all_pancakes_smiling_list = []
    for x in range(number_of_test_cases):
        flips_required, all_pancakes_smiling = flip_pancakes_to_happy_side(pancake_text_list[x], pancake_flip_size_list[x])
        flips_required_list.append(flips_required)
        all_pancakes_smiling_list.append(all_pancakes_smiling)

    output_results_to_file(flips_required_list, all_pancakes_smiling_list)

    return

if __name__ == "__main__":
    flip_pancake_cases_to_happy_side()