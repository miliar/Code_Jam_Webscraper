#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
# from numpy import *

fn = 'A-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    
    line = f.readline().split()
    N = int(line[0])
    
    commands = zip(line[1::2],[int(l) for l in line[2::2]])
    print commands
    
    op = 1
    bp = 1
    for t in range(1,100*101):
        
        onxt = filter(lambda x: x[0] == 'O',commands)
        bnxt = filter(lambda x: x[0] == 'B',commands)
        
        robot,command = commands[0]
        pushed = False
        if onxt:
            onxt = onxt[0]
            if onxt[1] > op:
                op += 1
            elif onxt[1] < op:
                op -= 1
            elif command == op and robot == 'O':
                pushed = True
            
        if bnxt:
            bnxt = bnxt[0]
            if bnxt[1] > bp:
                bp += 1
            elif bnxt[1] < bp:
                bp -= 1
            elif command == bp and robot == 'B':
                pushed = True
            
        if pushed:
            commands = commands[1:]            
            
        if not commands:
            final = t
            break
        
    ans = final
    
    fout.write('Case #%d: %s\n'%(case+1,ans))
    
