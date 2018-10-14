INFILE = r'C:\Users\noam\workspace\CodeJam\input.txt'

DONE_ALL = 'DONE_ALL'
PRESSED_CUR_TARGET = 'PRESSED_CUR_TARGET'
ADVANCED_TO_TAGET = 'ADVANCED_TO_TAGET'
STAYED_IN_PLACE = 'STAYED_IN_PLACE'

class Robot(object):
    def __init__(self, buttons, name):
        self.cur_pos = 1
        self.cur_target_idx = 0
        self.cur_target_pressed = False
        self.buttons = buttons
        self.done = len(buttons) == 0
        self.name = name
    
    def is_in_target(self):
        return self.cur_pos == self.buttons[self.cur_target_idx]
    
    def get_cur_target(self):
        return self.buttons[self.cur_target_idx]
    
    def print_cur_state(self):
        print 'Name:', self.name
        print 'cur_pos', self.cur_pos
        print 'cur_target', self.get_cur_target()
        print 'pressed cur target', self.cur_target_pressed
        
    def play_turn(self, my_turn):
        if self.done:
            return DONE_ALL
        
        if not self.is_in_target():
            self.cur_target_pressed = False
            if self.get_cur_target() < self.cur_pos:
                self.cur_pos -= 1
            else:
                self.cur_pos += 1
            return ADVANCED_TO_TAGET
        
        if my_turn:
            #press
            self.cur_target_pressed = True
            if self.cur_target_idx == len(self.buttons) - 1:
                self.done = True
                return PRESSED_CUR_TARGET
            self.cur_target_idx += 1
            return PRESSED_CUR_TARGET
        
        return STAYED_IN_PLACE
        
def calc_min_turns(buttons):
    if not buttons:
        return 0
    buttons.sort()
    push_turns = len(buttons)
    steps_for_max_button = max(buttons)
    return push_turns + steps_for_max_button
    
def parse_line(line):
    splitted = line.split(' ')[1:]
    robot_codes = splitted[0::2]
    buttons = splitted[1::2]
    buttons_dict = {'B': [], 'O': []}
    for robot_code, button in zip(robot_codes, buttons):
        buttons_dict[robot_code].append(int(button))
    
    return robot_codes, buttons_dict['B'], buttons_dict['O'] 

def play(robot_turn_codes, b_buttons, o_buttons):
    blue_robot = Robot(b_buttons, 'blue')
    orange_robot = Robot(o_buttons, 'orange')
    turn_counter = 0
    cur_turn_idx = 0
    
    while (not blue_robot.done) or (not orange_robot.done):
        turn_counter += 1
        orange_turn = robot_turn_codes[cur_turn_idx] == 'O'
        blue_turn = robot_turn_codes[cur_turn_idx] == 'B'
        blue_ret = blue_robot.play_turn(blue_turn)
        orange_ret = orange_robot.play_turn(orange_turn)
        if PRESSED_CUR_TARGET in (blue_ret, orange_ret):
            cur_turn_idx += 1
        print 'turn %d : O: %s, B: %s' % (turn_counter, orange_ret, blue_ret)
        print 'cur pos: O: %d, B: %d' % (orange_robot.cur_pos, blue_robot.cur_pos)
        print 'done   : O: %s, B: %s' % (orange_robot.done, blue_robot.done)
    
    return turn_counter
    
def main():
    infile = file(INFILE)
    outfile = file(INFILE + '.result.txt', 'wt')
    infile.readline()
    for idx, line in enumerate(infile):
        robot_turn_codes, b_buttons, o_buttons = parse_line(line)
        res = play(robot_turn_codes, b_buttons, o_buttons)
        res_line = 'Case #%d: %d\n' % (idx + 1, res)
        print res_line,
        outfile.write(res_line)
    infile.close()
    outfile.close()
    
if __name__ == '__main__':
    main()