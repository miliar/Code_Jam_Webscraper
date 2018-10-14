import sys, math, random
from copy import copy
 
sys.setrecursionlimit(10000)

f = open('data/A-small-attempt1.in', 'r')
o = open('data/A-small-attempt1.out', 'w')

t = f.readline().strip();

for i in range(int(t)):    
    alien_number = f.readline().strip()
    
    # Decide base
    chars = {}
    pos = len(alien_number)-1
    for c in alien_number:
        if chars.has_key(c):
            chars[c]+=1*math.pow(10, pos)
        else:
            chars[c]=1*math.pow(10, pos)
        pos-=1;
        
    base = len(chars)
    char_map_t = []
    char_map_t.append(1)
    char_map_t.append(0)
    
    if base == 1:
        print str(i) + " " + str(base)
        base+=1
    
    for j in range(2, base):
        char_map_t.append(j)
    
    char_map = {}
    for c in char_map_t:
        max_c = ''
        max_w = -1
        for char, w in chars.iteritems():
            if w > max_w:
                max_w = w
                max_c = char
        if max_c == '':
            continue
        del chars[max_c]
        char_map[max_c] = c
        
    number = 0
    pos = len(alien_number)-1
    for c in alien_number:
        number+=char_map[c]*math.pow(base, pos)
        pos-=1
    
    o.write("Case #" + str(i+1) + ": " + str(int(number)) + "\n")
    o.flush()
    
    