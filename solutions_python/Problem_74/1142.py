'''
Created on 2011-05-06

@author: Jordan Klassen
'''

import Tkinter
import tkFileDialog
def getInputFile():
    tkroot = Tkinter.Tk()
    tkroot.wm_state('withdrawn')
    out = tkFileDialog.askopenfile(parent=tkroot)
    tkroot.destroy()
    return out

#import sys
#outstrm = sys.stdout

import os
outstrm = open(os.path.expanduser("~/Desktop/out.txt"), 'w')

if __name__ == '__main__':
    file = getInputFile()
    if(file == None):
        exit(-1)
    cur = file.readline()
    num_cases = int(cur, 10)
    
    for i in range(0,num_cases):
        print i+1, '---------------------------------------------'
        cur = file.readline()
        cur = cur.split()
        o_pos = b_pos = 1
        time_buffer = 0
        buffer_blue = True
        
        # each button's going to take a second to be pressed anyways.
        time = 0#int(cur[0]);
        last = -1
        for j in range(0, int(cur[0])):
            print j, ':', cur[1 + j*2], cur[2 + j*2],
            target = int(cur[2 + j * 2])
            is_orange = cur[1 + j * 2].upper() == 'O'
            tmp_pos = o_pos if is_orange else b_pos
            turn_time = abs(tmp_pos - target) + 1
            if(is_orange == buffer_blue):
                if (turn_time <= time_buffer):
                    time_buffer = 1
                    time += 1
                    print 'extra',
                else:
                    time_buffer = turn_time - time_buffer
                    time += time_buffer
                    print 'added',
                buffer_blue = not is_orange
            else:
                time_buffer += turn_time
                time += turn_time
                print 'absolute',
            if is_orange:
                o_pos = target
            else:
                b_pos = target
            print time
        outstrm.write('Case #' + str(i+1) + ': ' + str(time) + '\n')
    exit(0)
    