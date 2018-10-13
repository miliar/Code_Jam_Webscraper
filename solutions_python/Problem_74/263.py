#!/usr/bin/env python
#-*- coding:utf-8 -*-

#filename = 'bots.in'
filename = 'A-large.in'

file=open(filename)

class Bot:
    def __init__(self, symbol):
        self.pos = 1
        self.symbol = symbol
        
    def goto_and_press(self, dest):
        if dest > self.pos: 
            self.log(dest, 'step+')
            self.pos += 1

            return 'step+'
            
        if dest < self.pos:
            self.log(dest, 'step-')
            self.pos -= 1

            return 'step-'
        
        if dest == self.pos and tura == self:
            self.log(dest, 'done - pressed')
            return 'done'
        else:
            raise "nie powinno się wydarzyć"
            self.log(dest, 'waiting')
            return 'waiting'
            
    def goto(self, dest):
        if dest==None: 
            self.log(-1, 'już nieaktywny' )
            return
    
        if dest > self.pos: 
            self.log(dest, 'step+')
            self.pos += 1

            return 'step+'
            
        if dest < self.pos:
            self.log(dest, 'step-')
            self.pos -= 1

            return 'step-'
            
        if dest == self.pos:
            self.log(dest, 'waiting')
            return 'waiting'

    def log(self, dest, status):
        return
        print "Bot %s, pozycja: %i, dest: %i, czynność: %s" % (self.symbol, self.pos, dest, status) 
            

tura=None    

for case in range(int(file.readline())):
    
    line_raw = file.readline()

    orange = Bot('O')
    blue = Bot('B')

# input
# 4 O 2 B 1 B 2 O 4

    line = line_raw.split()

    line=line[1:]  # wywalamy liczbę przycisków, mamy : B 2 B 1

    #zrobić z tego listę tupli [('o', 4), ('b', 12), .... ]
    moves = []
    while len(line):
        moves.append((line[0], int(line[1])))
        line=line[2:]
 
    
    next_move = 0
    time = 0

    while True:

        time+=1
        
#        print 'time: %i' % time
                
        # ktory bot ma teraz ruch >
        if moves[next_move][0] == 'O':
            tura, other = orange, blue
        else:
            tura, other = blue, orange
        
#        print 'tura: %s, other: %s' % (tura.symbol, other.symbol)

        # znaleźć cel dla drugiego bota
        other_dest=None
        for mv in moves[next_move:]:
            if other.symbol == mv[0]:
                other_dest=mv[1]
                break
                
        other.goto(other_dest)
        
        result = tura.goto_and_press(moves[next_move][1])
        
        if result=='done':
            next_move += 1
            
        if next_move > len(moves)-1: break
    
    output= 'Case #%i: %i' % ( case+1, time)
    print output   
    
