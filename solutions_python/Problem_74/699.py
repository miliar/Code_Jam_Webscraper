#!/usr/bin/env python

import re
import sys
import logging

PUSHED = []
INPUT_FILE=file('A-large.in')
OUTPUT_FILE=file('A-large.out', 'w')

class Robot(object):

    def __init__(self, name, moves):
        self.position = 1
        self.moves = moves
        self.name = name
        self.code = name[0]
        logging.debug("My name is %s and I'll follow the path %s", self.name, 
                                                                   self.code)
    
    def walk_forward(self):
        self.position += 1
        logging.debug('%s move to button %s', self.name, self.position)
    
    def walk_backwards(self):
        self.position -= 1
        logging.debug('%s move to button %s', self.name, self.position)

    def push_button(self):  
        self.moves.pop(0)
        PUSHED.append(True)
        logging.debug('%s pushing button %s', self.name, self.position)
   
    @property
    def goal(self):
        if not len(self.moves):
            return 
 
        for move in self.moves:
            if move.startswith(self.code):
                return int(move.split(' ')[1])
    
    @property
    def my_turn(self):
        if PUSHED:
            return False
        if len(self.moves):
            return self.moves[0].startswith(self.code)

    def act(self):
        if self.goal:
            if self.my_turn and self.position == self.goal:
                self.push_button()
            elif self.position > self.goal:
                self.walk_backwards()
            elif self.position < self.goal:
                self.walk_forward()


def press_the_buttons(n, moves):
    count = 0    
    
    orange = Robot('Orange', moves)
    blue = Robot('Blue', moves)

    while moves:
        count += 1 
        orange.act()
        blue.act() 
        if PUSHED:
            PUSHED.pop() 
    logging.debug('Moviments %s', count)
    return count 

NUM_REGEXP = re.compile('(^\d+)\s') 
SEQ_REGEXP = re.compile('([BO]\s\d+)')
def parse_line(line):
    n = int(NUM_REGEXP.findall(line)[0])
    moves = SEQ_REGEXP.findall(line)

    return n, moves

def main():
    line_num = 0
    for line in INPUT_FILE:
        if line_num == 0:
            line_num += 1
            continue
         
        n, moves = parse_line(line)
        count = press_the_buttons(n, moves) 
        OUTPUT_FILE.write("Case #%s: %s\n" % (line_num, count))
        line_num += 1
        
if __name__ == '__main__':
    #logging.root.setLevel(logging.DEBUG)
    main()
