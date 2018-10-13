import sys

class Robot:
    def __init__(self, buttons):
        self.position=1        # Initial robot position
        self.buttons=buttons   # A list of button positions
        self.button_idx=0      # Index to buttons
        
    def press_button(self):
        if self.button_idx>=len(self.buttons):
            return
        next_button_pos=self.buttons[self.button_idx]
        distance=abs(self.position-next_button_pos)
        self.position=next_button_pos
        self.button_idx+=1
        return distance+1
        
    def go_to_button(self, time):
        if self.button_idx>=len(self.buttons):
            return
        next_button_pos=self.buttons[self.button_idx]
        distance=min(abs(self.position-next_button_pos), time)
        if next_button_pos>self.position:
            self.position+=distance
        else:
            self.position-=distance
        
    def __str__(self):
        if self.button_idx>len(self.buttons):
            return "Finished"
        return 'Position: %-4d   Buttons:%-15s    Button_index=%-4d' % \
            (self.position, self.buttons, self.button_idx)
        



lines=sys.stdin.readlines()[1:]
case_count=1
for line in lines:
    line=line.split()
    missions=[i for i in line if i in ('O', 'B')]
    orange_buttons,blue_buttons=[],[]
    for i in range(len(line)):
        if line[i]=='O':
            orange_buttons.append(int(line[i+1]))
        elif line[i]=='B':
            blue_buttons.append(int(line[i+1]))
    
    total_time=0
    orange, blue = Robot( orange_buttons ), Robot( blue_buttons )
    for mission in missions:    
        if mission=='O':
            time=orange.press_button()
            blue.go_to_button(time)
        else:
            time=blue.press_button()
            orange.go_to_button(time)
        total_time+=time
            
    print 'Case #%d: %d' % (case_count, total_time)
    case_count+=1