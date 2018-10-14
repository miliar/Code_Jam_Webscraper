"""
    
    Name    : Qualification.py

    Usage    : Qualification.py input_file

    Author    : Bar Harel

    Description:
        - Qualification round of Google CodeJam

    Changelog:
        - 11/04/15 - Creation
"""

import sys

OUTPUT_PATH = "output.txt"

def calculate_case(max_shyness, dataset_string):
    """
        Function     : calculate_case(max_shyness, dataset_string) --> number_of_friends
        
        Purpose:
            - Given a max_shyness and a dataset string, this function will calculate the number of friends needed to invite.
        
        Remarks:
            - 
    """
    guest_count = 0
    friends_needed = 0

    # For each shyness level
    for shyness_level in range(max_shyness+1):

        # Check if there are enough guests to meet the quota
        if guest_count < shyness_level:
            # If not, increase the amount of friends needed
            friends_needed += shyness_level-guest_count
            guest_count += shyness_level-guest_count

        # Guest count
        guest_count += int(dataset_string[shyness_level])

    return friends_needed

def main():
    """
        Function: main() --> NoneType
        
        Purpose:
            - Control the flow of the program
    """
    with open(sys.argv[1]) as input_file:
        # Fetch the test cases
        test_cases = int(input_file.readline())

        # Initialize case list
        case_list = []
        
        # Take cases from input, and convert to list
        for curr_case in range(test_cases):
            # Take case string
            case = input_file.readline()
            # Split
            max_shyness, dataset = case.split()
            # Append to the case list
            case_list.append((int(max_shyness), dataset))

    output_string = ""

    # For each case, calculate output and print
    for case_number in range(1,test_cases+1):
        output_string += "Case #%d: %d\n" % (case_number, calculate_case(*case_list[case_number-1]))

    # Strip the excess newline
    output_string = output_string.rstrip()

    # Write the output file
    with open(OUTPUT_PATH, "w") as output_file:
        output_file.write(output_string)

if __name__ == "__main__":
    main()