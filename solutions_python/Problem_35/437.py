import sys
from copy import copy
 
f = open('/home/moha/pre-releases/code-jam/B-small-attempt2.in', 'r')
o = open('/home/moha/pre-releases/code-jam/B-small-attempt2.out', 'w')

n = f.readline().strip();

for i in range(int(n)):
    (h, w) = f.readline().strip().split(' ');

    h = int(h)
    w = int(w)
    
    land = []
    
    for j in range(int(h)):
        land.append(f.readline().strip().split(' '));
        
    basins = {}
    basins[0] = 0
    last_sink = 0
    
    for j in range(int(h)):
        for k in range(int(w)):
            curr = land[j][k]
            
            sink = last_sink+1
            
            min = curr 
            cp = (j*w)+k
            mp = cp
            
            if j < h-1 and min >= land[j+1][k]:
                mp = ((j+1)*w)+k
                min = land[j+1][k]
                
            if k < w-1 and min >= land[j][k+1]:
                mp = (j*w)+k+1
                min = land[j][k+1]
                
            if k > 0 and min >= land[j][k-1]:
                mp = (j*w)+k-1
                min = land[j][k-1]
                
            if j > 0 and min >= land[j-1][k]:
                mp = ((j-1)*w)+k
                min = land[j-1][k]
 
            if min == curr:
                mp = cp
                
            if basins.has_key(mp):
                sink = basins[mp]
                if basins.has_key(cp):
                    for _cp in basins:
                        if basins[_cp] == basins[cp]:
                            basins[_cp] = sink
                            
                basins[cp] = sink
            elif basins.has_key(cp):
                sink = basins[cp]
                basins[mp] = sink
            else:
                sink = last_sink+1
                basins[cp] = sink
                basins[mp] = sink
                
            if sink == last_sink+1:
                last_sink+=1
         
    o.write("Case #" + str(i+1) + ":\n")
     
    words = []
    
    """
    for x in range(26):
        _word = []
        for j in range(int(h)):
            for k in range(int(w)):
                if (basins[(j*w)+k] == x):
                    _x = 0
                elif (basins[(j*w)+k] == 0):
                    _x = x
                else:
                    _x = basins[(j*w)+k]
                _word.append(chr(97+_x))
        words.append(' '.join(_word))
        
        for j in range(int(h)):
            for k in range(int(w)):
               _x = basins[(j*w)+k]+x%26
               _word.append(chr(97+_x))
        words.append(' '.join(_word))
        
    words = sorted(words)
    """
    
    lbc = 0
    bc = {}
    _word = []
    for j in range(int(h)):
        for k in range(int(w)):
            if bc.has_key(basins[(j*w)+k]):
                _x = bc[basins[(j*w)+k]]
            else:
                _x = lbc
                bc[basins[(j*w)+k]] = _x
                lbc+=1    
            _word.append(chr(97+_x))
            
    words.append(' '.join(_word))
        
    wordx = words[0].split(' ')
    for j in range(int(h)):
        o.write(' '.join(wordx[j*w:j*w+w]) + "\n")
        