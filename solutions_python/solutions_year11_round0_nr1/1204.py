#!/usr/bin/env python

import sys

class b:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]

class Move:
    """
    """
    def __init__(self, n_move, move):
        self.n_move = n_move
        self.move = move

class Robot:
    """
    """
    def __init__(self, moves):
        self.moves = moves
        self.moves.reverse()
        self.current_move = None
        if len(moves) > 0:
            self.current_move = moves.pop()
        self.current_position = 1
    
    def do_move(self, n_move):
        """
        
        Arguments:
        - `self`:
        """
        if self.current_move is None:
            return False
        
        if self.current_move.n_move == n_move:
            if self.current_position == self.current_move.move:
                if len(self.moves) == 0:
                    self.current_move = None
                else:
                    self.current_move = self.moves.pop()
                return True
            else:
                if self.current_position < self.current_move.move:
                    self.current_position += 1
                elif self.current_position > self.current_move.move:
                    self.current_position -= 1
        else:
            if (self.current_position < self.current_move.move):
                self.current_position += 1
            elif self.current_position > self.current_move.move:
                self.current_position -= 1
        return False
        
def go():
    """
    Starts the program.
    """
    t = b.line(int)
    for i in range(t):
        moves = b.splitline()
        moves_orange, moves_blue = [], []
        n_moves = int(moves[0])

        for j in range(n_moves):
            index = j*2+1
            move = Move(j+1, int(moves[index+1]))
            if (moves[index] == 'O'):
                moves_orange.append(move)
            else:
                moves_blue.append(move)
                
        orange_robot = Robot(moves_orange)
        blue_robot = Robot(moves_blue)
        n_move, time = 0, 0
        while n_move < n_moves:
            orange_move = orange_robot.do_move(n_move+1)
            blue_move = blue_robot.do_move(n_move+1)
            if orange_move or blue_move:
                n_move += 1
            time += 1

        print b.case(),
        print time
                
go()

