'''
Created on 07.05.2011

@author: ikari
'''

class push_sequences:
    def init(self):
        self.orange_buttons = []
        self.orange_index = 0
        self.orange_pos = 0
        
        self.blue_buttons = []
        self.blue_index = 0
        self.blue_pos = 0
        
        self.queue = []
        self.q_index = 0
        
    def solve(self):
        answer = 0
        
        while self.q_index < len(self.queue):
            blue_togo = abs(self.blue_pos - self.blue_buttons[self.blue_index])
            orange_togo = abs(self.orange_pos - self.orange_buttons[self.orange_index])
            
            if blue_togo == 0 and self.queue[self.q_index] == 'B':
                self.q_index += 1
                self.blue_index += 1
                answer += 1
                
                if self.orange_pos > self.orange_buttons[self.orange_index]:
                    self.orange_pos -= 1
                elif self.orange_pos < self.orange_buttons[self.orange_index]:
                    self.orange_pos += 1
              
                continue
            
            if orange_togo == 0 and self.queue[self.q_index] == 'O':
                self.q_index += 1
                self.orange_index += 1                
                answer += 1
                
                if self.blue_pos > self.blue_buttons[self.blue_index]:
                    self.blue_pos -= 1
                elif self.blue_pos < self.blue_buttons[self.blue_index]:
                    self.blue_pos += 1
                
                continue
            
            if self.queue[self.q_index] == 'O':
                answer += orange_togo
                self.orange_pos = self.orange_buttons[self.orange_index]
                
                if orange_togo < blue_togo:
                    if self.blue_pos > self.blue_buttons[self.blue_index]:
                        self.blue_pos -= orange_togo
                    else:
                        self.blue_pos += orange_togo
                else:
                    self.blue_pos = self.blue_buttons[self.blue_index]
        
            if self.queue[self.q_index] == 'B':
                answer += blue_togo
                self.blue_pos = self.blue_buttons[self.blue_index]
                
                if blue_togo < orange_togo:
                    if self.orange_pos > self.orange_buttons[self.orange_index]:
                        self.orange_pos -= blue_togo
                    else:
                        self.orange_pos += blue_togo
                else:
                    self.orange_pos = self.orange_buttons[self.orange_index]
                    
        return answer

def create_push_sequences(ss):
    ret = push_sequences()
    ret.init()
    
    for i in range(1, len(ss), 2):
        sym = ss[i]
        num = int(ss[i+1])
        
        ret.queue.append(sym)
        
        if sym == 'O':
            ret.orange_buttons.append(num - 1)
        else:
            ret.blue_buttons.append(num - 1)
   
    ret.orange_buttons.append(0)
    ret.blue_buttons.append(0)
    return ret

filename = "input.txt"
f = open(filename, "r")

T = int(f.readline())

for i in range(0, T):
    ss = f.readline().split()
    seq = create_push_sequences(ss)
    print 'Case #' + str(i + 1) + ': ' + str(seq.solve())
    
