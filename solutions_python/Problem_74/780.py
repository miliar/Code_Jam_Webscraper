'''
Created on 06/mag/2011

@author: Luca Pinello

INPUT
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

OUTPUT
Case #1: 6
Case #2: 100
Case #3: 4
'''

fout=open('bot_trust_output.txt','w+')
fin=open('./input.txt','r')
N_BUTTONS=100

class Bot:
    current_position=None
    working=False
    target=None
    
    def __init__(self,n_buttons):
        self.current_position=1
        
    def move_forward(self):
        self.current_position+=1
    
    def move_backward(self):
        self.current_position-=1
        
    def set_target(self,button_position):
        self.target=button_position
    
    def target_reached(self):
        return self.current_position==self.target
    
    def approach_target(self):
        if self.target==self.current_position:
            pass
        elif self.target>self.current_position:
            self.move_forward()
        else:
            self.move_backward()


if __name__ == '__main__':

    T=int(fin.readline())    
    for i in range(T):
        line=fin.readline()    
        moves=line.split()
        
        n_moves=int(moves[0])
        moves=moves[1:]
       
        blue_bot=Bot(N_BUTTONS)
        orange_bot=Bot(N_BUTTONS)
        
        if 'B' in moves:
            blue_bot.set_target(int(moves[moves.index('B')+1]))
                    
        if 'O' in moves:
            orange_bot.set_target(int(moves[moves.index('O')+1]))
        
        current_turn=moves[0]
       
        sequence_completed=False
        current_time=0
        button_pressed=False
        
        while not sequence_completed:
            current_time+=1
            
            if current_turn=='B':
                if blue_bot.target_reached():
                    button_pressed=True
                else:
                    blue_bot.approach_target()
                                
                orange_bot.approach_target()
            
            else:    
                if orange_bot.target_reached():
                    button_pressed=True
                else:
                    orange_bot.approach_target()
                                
                blue_bot.approach_target()
            
            if button_pressed:
                moves=moves[2:] 
                button_pressed=False
                
                if moves:
           
                    if 'B' in moves:
                        blue_bot.set_target(int(moves[moves.index('B')+1]))
                    
                    if 'O' in moves:
                        orange_bot.set_target(int(moves[moves.index('O')+1]))
                    
                    current_turn=moves[0]
           
                else:
                    sequence_completed=True
        fout.write( 'Case #%d: %d\n' %(i+1,current_time) )
fout.close()
