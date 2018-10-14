__author__ = 'jamesbutler'


def calculate_friends_needed(max_shyness, shyness_levels):
    friends_needed = 0
    audience_members_clapping = 0
    for i in range(len(shyness_levels)):
        if audience_members_clapping <= i:
            difference = i - audience_members_clapping
            friends_needed += difference
            audience_members_clapping += difference
        audience_members_clapping += int(shyness_levels[i])
        if audience_members_clapping >= int(max_shyness):
            return friends_needed
    return friends_needed


def main():
    output_file = open("output.txt", "w")
    with open("input.txt", "r") as input_file:
        number_of_test_cases = input_file.readline().strip()
        for i in range(int(number_of_test_cases)):
            line = input_file.readline()
            max_shyness, shyness_levels = line.split()
            friends_needed = calculate_friends_needed(max_shyness, shyness_levels)
            output_file.write("Case #" + str(i+1) + ": " + str(friends_needed) + "\n")
    output_file.close()

if __name__ == "__main__":
    main()