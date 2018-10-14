#!/usr/bin/python

import sys

_line = lambda : sys.stdin.readline()

def line(*args):
	L = _line().strip().split()
	L = zip( L, list(args) + [str]*(len(L)-len(args)) )
	return [ type(data) for data, type in L ]	
	
def iline(): return map( int, _line().strip().split() )
def fline(): return map( float, _line().strip().split() )

def setLineInput(input_file):
	global _line
	_line = lambda : input_file.readline()
	

    
import heapq

class heap:
    def __init__(self, data=[], key=None):
        self.__key = key
        if self.__key:
            self.__heap = [ (self.__key(x), x) for x in data ]
        else:
            self.__heap = list(data)
        heapq.heapify( self.__heap )
        
    def push(self, x):
        if self.__key:
            x = (self.__key(x), x)
        heapq.heappush( self.__heap, x )
        
    def pop(self):
        x = heapq.heappop( self.__heap )
        return x[1] if self.__key else x