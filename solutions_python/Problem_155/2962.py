__author__ = 'madanrp'
import sys

def get_output(test_case):
    max_shy, bit_string = test_case.split(" ", 1)
    max_shy = int(max_shy)
    bit_str_len = len(bit_string)

    people_resource = []
    people_needed = 0
    for i in range(bit_str_len):
        ith_member = int(bit_string[i])
        if i > 0 and ith_member > 0:
            prev_sum = people_resource[i-1]
            if prev_sum < i:
                people_resource[i - 1] += i - prev_sum
                people_needed += i - prev_sum
        if i > 0:
            ith_member = ith_member + people_resource[i-1]
        people_resource.append(ith_member)
    return people_needed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(-1)
    file = sys.argv[1]
    lines = open(file).readlines()
    num_test = int(lines[0].strip())
    with open("output.txt", "w") as f:
        for i in range(num_test):
            test_case = lines[i+1].strip()
            output = get_output(test_case)
            f.write("Case #" + str(i+1) + ": " + str(output))
            f.write("\n")

