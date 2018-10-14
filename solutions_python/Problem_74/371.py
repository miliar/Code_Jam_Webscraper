#infile = open("A-small-attempt0.in")
#outfile = open("A-small.out",'w')
infile = open("A-large.in")
outfile = open("A-large.out",'w')
case = 1
lines = infile.readlines()
cases = int(lines[0])
del lines[0]
for line in lines:
    orange = []
    blue = []
    buttons = []
    data = line.split()
    num_buttons = int(data[0])
    button = 1
    while button <= num_buttons*2:
      if 'O' in data[button]:
        orange.append(int(data[button+1]))
      else:
        blue.append(int(data[button+1]))
      buttons.append((data[button],int(data[button+1])))
      button = button+2
    
    blue_pos = 0
    orange_pos = 0
    rounds=0

    while len(buttons)>0:
        if 'O' in buttons[0][0]:
            if orange_pos == buttons[0][1]:
                del buttons[0]
                del orange[0]
            elif orange_pos < buttons[0][1]:
                orange_pos=orange_pos+1
            else:
              orange_pos=orange_pos-1
            if len(blue)>0:
                if blue_pos > blue[0]:
                    blue_pos=blue_pos-1
                elif blue_pos < blue[0]:
                    blue_pos=blue_pos+1
        elif 'B' in buttons[0][0]:
            if blue_pos == buttons[0][1]:
                del buttons[0]
                del blue[0]
            elif blue_pos < buttons[0][1]:
                blue_pos=blue_pos+1
            else:
              blue_pos=blue_pos-1
            if len(orange)>0:
                if orange_pos > orange[0]:
                    orange_pos= orange_pos -1
                elif orange_pos < orange[0]:
                    orange_pos= orange_pos +1
        rounds+=1


        
    rounds -=1
    outfile.write( "Case #%d: %d\n" % (case, rounds))
    case +=1

infile.close()
outfile.close()
