import sys
import re

# Deceitful War Pseudocode:
# while unfinished:
#     if min(Naomi) < min(Ken):
#         Tell Ken we have max(Ken) - epsilon.
#         Ken plays max(Ken) while Naomi plays min(Naomi).
#         Increment Score_Ken.
#     elif min(Ken) <= min(Naomi):
#         Tell Ken we have max(Ken) + epsilon.
#         Ken plays min(Ken) to throw the round while Naomi plays min(Naomi).
#         Increment Score_Naomi.

# How to determine epsilon:
# -epsilon:   Average top two scores that Ken has.
# +epsilon:   Find some really small number which we increment each time we hit this case.

def parse_input(input_file, output_file):
    num_tests = -1
    curr_datum = {"num_blocks": 0, "naomi": None, "ken": None}
    curr_field = 0
    test_num = 1

    with open(input_file, "r") as f_in:
        with open(output_file, "w") as f_out:
            for line in f_in:
                if num_tests == -1:
                    num_tests = int(line)
                else:
                    if curr_field == 0:
                        curr_datum["num_blocks"] = int(line)
                    elif curr_field == 1:
                        block_weights = re.findall(r'[0-9.]+', line)
                        curr_datum["naomi"] = [float(block) for block in block_weights]
                    else:
                        block_weights = re.findall(r'[0-9.]+', line)
                        curr_datum["ken"] = [float(block) for block in block_weights]
                        war_score = simulate_war(curr_datum)
                        deceitful_war_score = simulate_deceitful_war(curr_datum)
                        write_output(f_out, test_num, deceitful_war_score, war_score)
                        test_num += 1

                    curr_field = (curr_field + 1) % 3

def simulate_war(curr_datum):
    naomi_blocks, ken_blocks = list(curr_datum["naomi"]), list(curr_datum["ken"])
    naomi_blocks.sort()
    ken_blocks.sort()
    naomi_score, ken_score = 0, 0

    while len(naomi_blocks) != 0:
        naomi_curr = naomi_blocks.pop(0)
        ken_curr = None
        for i in range(len(ken_blocks)):
            ken_curr = ken_blocks[i]
            if ken_curr > naomi_curr:
                ken_curr = ken_blocks.pop(i)
                break

        if naomi_curr > ken_curr:
            naomi_score += 1
        else:
            ken_score += 1

    return naomi_score

def simulate_deceitful_war(curr_datum):
    naomi_blocks, ken_blocks = list(curr_datum["naomi"]), list(curr_datum["ken"])
    naomi_blocks.sort()
    ken_blocks.sort()
    naomi_score, ken_score = 0, 0

    while len(naomi_blocks) != 0:
        naomi_curr = naomi_blocks.pop(0)    # min(Naomi)
        if naomi_curr < min(ken_blocks):
            ken_curr = ken_blocks.pop() # max(Ken)
        else:
            ken_curr = ken_blocks.pop(0)    # min(Ken)

        # print("naomi_curr: " + str(naomi_curr) + "  ken_curr: " + str(ken_curr))
        if naomi_curr > ken_curr:
            naomi_score += 1
        else:
            ken_score += 1

    return naomi_score

def write_output(file_handle, test_num, value1, value2):
    file_handle.write("Case #" + str(test_num) + ": " + str(value1) + " " + str(value2) + "\n")
    print("Wrote output for test case: " + str(test_num))

if __name__=='__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = "deceitful_war.out"
        parse_input(input_file, output_file)
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        parse_input(input_file, output_file)
    else:
        print("Incorrect number of arguments supplied: " + str(len(sys.argv)))