'''
Created on May 7, 2011

@author: karnr
'''
from collections import defaultdict

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        test_input = fh.readline().strip().split()
        num_of_buttons = int(test_input[0])
        idx = 1
        button_sequence = list()
        while (idx < (2 * num_of_buttons)):
            button_sequence.append((test_input[idx], int(test_input[idx + 1])))
            idx = idx + 2
                        
        test_data[count] = button_sequence
        count = count + 1
    
    fh.close()
    return test_data
    
def _move_bot(src, dst, allowed_time):
    step_size = 1
    if (src > dst):
        step_size = -1
        
    curr = src
    time_taken = 0
    while (time_taken < allowed_time):
        if (curr == dst):
            break
        curr = curr + step_size
        time_taken = time_taken + 1
        
    return (curr, time_taken + 1)
        
def _update_time_since_last_move(ignr_type, time_since_last_move, time):
    for bot_type in time_since_last_move.keys():
        if (bot_type == ignr_type):
            time_since_last_move[bot_type] = 0
        else:
            time_since_last_move[bot_type] = time_since_last_move[bot_type] + time
            
def _execute_test(test_data):
    
    bot_button_sequence = defaultdict(list)
    for (bot_type, button) in test_data:
        bot_button_sequence[bot_type].append(button)
        
    bot_state = dict([(bot_type, 1) for bot_type in bot_button_sequence.keys()])
   
    time_since_last_move = dict([(bot_type, 0) for bot_type in bot_button_sequence.keys()])
    
    bot_last_moved = None
    time_taken = 0
    print "======== Executing Test with data: %s" % test_data
    for (bot_type, button) in test_data:
        
        curr_state = bot_state[bot_type]
        
        if (bot_last_moved is not None) and (bot_last_moved != bot_type):
            time_elapsed = time_since_last_move[bot_type]
            print "Updating bot: %s state from %s to %s" % (bot_type, curr_state, button)
            (curr_state, bot_time) = _move_bot(curr_state, button, time_elapsed)
            print "Bot: %s already reached till %s in last %s seconds" % (bot_type, curr_state, time_elapsed)
        
        bot_last_moved = bot_type
        
        print "Moving bot: %s from %s to %s" % (bot_type, curr_state, button)
        (curr_state, bot_time) = _move_bot(curr_state, button, 9999999999999)
        bot_state[bot_type] = button
        print "Took time: %s seconds" % bot_time   
        
        _update_time_since_last_move(bot_type, time_since_last_move, bot_time)
        time_taken = time_taken + bot_time
        
    return time_taken

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()