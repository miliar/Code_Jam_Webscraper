#!/usr/bin/env python2

import sys

def process(input_file):
    
    fd = open(input_file, 'r')

    num_tests = int(fd.readline())

    for i in xrange(1, num_tests+1):
        
        line = fd.readline()[:-1]
        print 'Case #%d:' %  i,
        
        #butt_num = int(line[0])
        
        blue_pos = 1
        orange_pos = 1
        
        time = 0

        seq = line.split()
        seq = seq[1:]
        
        orange_gain = 0 
        blue_gain = 0

        #print seq

        while len(seq) != 0:
           
            color = seq[0]
            button_pos = int(seq[1])

            if color == 'O': # orange bot
                direction = 1
                if button_pos < orange_pos:
                    direction = -1
                
                # move to the next position
                for j in xrange(orange_pos+direction, button_pos+direction, direction):
                    
                    orange_pos = j
                    
                    if blue_gain > 0:
                        blue_gain -= 1
                    else:
                        orange_gain += 1
                        time += 1 

                # press the button
                time += 1
                orange_gain += 1
                blue_gain = 0

            else: # blue bot
                direction = 1
                if button_pos < blue_pos:
                    direction = -1
               
                # move to the next position
                for j in xrange(blue_pos + direction, button_pos+direction, direction):
                     
                    blue_pos = j

                    if orange_gain > 0:
                        orange_gain -= 1
                    else:
                        blue_gain += 1
                        time += 1 

                # press the button
                time += 1
                blue_gain += 1
                orange_gain = 0
            
            #print 'color', color, 'button position', button_pos, 'blue_pos', blue_pos, 'orange_pos', orange_pos
            #print 'orange_gain', orange_gain
            #print 'blue gain', blue_gain
            #print 'current time', time
            seq = seq[2:]

        print time


if __name__ == '__main__':
    
    #process('small.in')
    process('large.in')
    #process('sample.in')

