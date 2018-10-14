import re
import sys

input_file_name = sys.argv[1]
out_file_name = sys.argv[2]
output_data = open(out_file_name, 'w')
with open(input_file_name) as data:
    number_of_test_case = int(data.readline().strip())
    for index in range(number_of_test_case):
        friends_required = 0
        shyness_aggregate = 0
        line_data = data.readline().split()
        max_shy = line_data[0]
        shy_string = line_data[1]
        for shyness_index, num_string in enumerate(shy_string):
            num = int(num_string)
            if shyness_index > shyness_aggregate:
                friends_required += shyness_index - shyness_aggregate
                shyness_aggregate = shyness_index
            shyness_aggregate += num
        string_to_print = "Case #{}: {}".format(index + 1, friends_required)
        print >> output_data, string_to_print
output_data.close()
