# -*- coding: utf-8 -*-

def doit():

    line = raw_input().split()
    moves_O = []
    moves_B = []
    
    for i in xrange(1, len(line), 2):
        r = line[i]
        pos = int(line[i+1])
        if (r == 'O'):
            moves_O.append((i / 2 + 1, pos))
        else:
            moves_B.append((i / 2 + 1, pos))
    
    moves_O = list(reversed(moves_O))
    moves_B = list(reversed(moves_B))
    
    c_pos_O = 1
    c_pos_B = 1
    time = 0
    
    while moves_O and moves_B:
        i_O, n_pos_O = moves_O[-1]
        i_B, n_pos_B = moves_B[-1]
        
        if i_O > i_B:
            if c_pos_B == n_pos_B:
                del moves_B[-1]
            elif c_pos_B < n_pos_B:
                c_pos_B += 1
            else:
                c_pos_B -= 1
            
            if c_pos_O < n_pos_O:
                c_pos_O += 1
            elif c_pos_O > n_pos_O:
                c_pos_O -= 1
        else:
            if c_pos_O == n_pos_O:
                del moves_O[-1]
            elif c_pos_O < n_pos_O:
                c_pos_O += 1
            else:
                c_pos_O -= 1
            
            if c_pos_B < n_pos_B:
                c_pos_B += 1
            elif c_pos_B > n_pos_B:
                c_pos_B -= 1
        time += 1
    
    while moves_O:
        _, n_pos_O = moves_O[-1]
        if c_pos_O == n_pos_O:
            del moves_O[-1]
        elif c_pos_O < n_pos_O:
            c_pos_O += 1
        else:
            c_pos_O -= 1
        time += 1
    
    while moves_B:
        _, n_pos_B = moves_B[-1]
        if c_pos_B == n_pos_B:
            del moves_B[-1]
        elif c_pos_B < n_pos_B:
            c_pos_B += 1
        else:
            c_pos_B -= 1
        time += 1
    
    return time

T = input()

for t in xrange(1, T+1):
    ans = doit()
    print 'Case #%d: %d' % (t, ans)