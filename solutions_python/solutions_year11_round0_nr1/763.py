#probably the ugliest code I ever written (except in school maybe)

import sys, math
    
def main():
    if len(sys.argv) < 2:
        print ('usage: python something.py input_filename')
        quit()
        
    f = open(sys.argv[1], 'r')
    out = open("out", 'w')
    
    cases = int(f.readline()) #number of cases
    
    for case in range(cases):    
        print '\nCase', case+1
        
        b_pos = 1 #position of Blue
        o_pos = 1 #position of Orange
        
        line = f.readline().split()
        n_buttons = int(line[0]) #number of buttons to be pressed
        
        i = 1
        time = 0
        buttons = []
        while i < len(line) - 1:
            buttons.append((line[i],int(line[i+1]))) # list of (robot, button)
            i += 2
        print buttons
        
        
        current = 0 #button pressed
        seconds = 0
        
        while (current < n_buttons):
            print "second", seconds
            b_next = -1
            o_next = -1
            b_pressed = False
            
            for i in range(current, n_buttons):
                if buttons[i][0] == 'B':
                    b_next = buttons[i][1]
                    b_order = i
                    print "B's next =", buttons[i]
                    break
                    
            for i in range(current, n_buttons):
                if buttons[i][0] == 'O':
                    o_next = buttons[i][1]
                    o_order = i
                    print "O's next =", buttons[i]
                    break
            
            if b_next != -1:
                if b_pos != b_next:
                    b_pos += int(math.copysign(1, (b_next-b_pos))) #1 move in direction
                    print "B moves", b_pos
                elif current == b_order:
                    current += 1 #press button
                    print "B presses"
                    b_pressed = True #to avoid o pressing after b
                else:
                    pass #wait  
                    print "B waits"
            
            if o_next != -1:
                if o_pos != o_next:
                    o_pos += int(math.copysign(1, (o_next-o_pos))) #1 move in direction
                    print "O moves", o_pos
                elif current == o_order and not b_pressed:
                    current += 1 #press button
                    print "O presses"
                else:
                    pass #wait
                    print "O waits"
            
            seconds += 1
        
        print "Total seconds:", seconds
                    
        out.write('Case #{0}: {1}\n'.format(case+1, seconds))
    out.close()
    
if __name__ == "__main__":
    main()