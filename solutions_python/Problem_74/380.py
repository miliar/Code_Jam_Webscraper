import re
import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )

def execute_instruction(instruction):
    robot_id, robot_instruction = instruction.split(" ")
    
    time_counter = 0
    while True:
        pushed = False
        for performing_robot_id in robot_queue:
            if perform_action(performing_robot_id, robot_id):
                pushed = True
        time_counter += 1
        if pushed:
            break
    
    return time_counter
            
def perform_action(performing_robot_id, robot_id_queued):
    
    if not robot_queue[performing_robot_id]: 
        return False
    
    cur_position = robot_positions[performing_robot_id]
    desired_position = robot_queue[performing_robot_id][0]
    
    if cur_position == desired_position:
        
        if performing_robot_id == robot_id_queued:
            # pushing the button
            robot_queue[performing_robot_id] = robot_queue[performing_robot_id][1:]
            return True
        
    elif cur_position < desired_position:
        robot_positions[performing_robot_id] += 1
    else:
        robot_positions[performing_robot_id] -= 1
        
    return False

ORANGE_ID = "O"
BLUE_ID = "B"

robot_queue = None
robot_positions = None
time_counter = None
input_f = open(sys.argv[1], "r")
output_f = open(sys.argv[2], "w")

TEST_CASES_NUM = int(input_f.readline())

seq_split_re = re.compile("(\w \d+)")
for test_case_i in xrange(TEST_CASES_NUM):
    time_counter = 0
    robot_queue = {ORANGE_ID: [], BLUE_ID: []}
    robot_positions = {ORANGE_ID: 1, BLUE_ID: 1}
    s = input_f.readline().strip()
    (seq_length, s) = s.split(" ", 1)
    seq_instructions = []
    for seq_instruction in seq_split_re.findall(s):
        seq_instructions.append(seq_instruction)
        robot_id, robot_instruction = seq_instruction.split(" ")
        robot_queue[robot_id].append(int(robot_instruction))
    
    # imitating stack
    seq_instructions.reverse()
    while seq_instructions:
        time_counter += execute_instruction(seq_instructions.pop())
        
    output_f.write("Case #%d: %s\n" % (test_case_i + 1, time_counter))

