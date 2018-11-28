import os

print(os.getcwd())
f = open('in.txt','r')
o = open ('out.txt','w')

cases = f.readline().strip()

case = 0
for l in f:
    case += 1
    
    newl = ''
    
    for c in l:
                                      
        if c == 'y': newl = newl + 'a'
        if c == 'n': newl = newl + 'b'
        if c == 'f': newl = newl + 'c'
        if c == 'i': newl = newl + 'd'
        if c == 'c': newl = newl + 'e'
        if c == 'w': newl = newl + 'f'
        if c == 'l': newl = newl + 'g'
        if c == 'b': newl = newl + 'h'
        if c == 'k': newl = newl + 'i'
        if c == 'u': newl = newl + 'j'
        if c == 'o': newl = newl + 'k'
        if c == 'm': newl = newl + 'l'
        if c == 'x': newl = newl + 'm'
        if c == 's': newl = newl + 'n'
        if c == 'e': newl = newl + 'o'
        if c == 'v': newl = newl + 'p'
        if c == 'z': newl = newl + 'q'
        if c == 'p': newl = newl + 'r'
        if c == 'd': newl = newl + 's'
        if c == 'r': newl = newl + 't'
        if c == 'j': newl = newl + 'u'
        if c == 'g': newl = newl + 'v'
        if c == 't': newl = newl + 'w'
        if c == 'h': newl = newl + 'x'
        if c == 'a': newl = newl + 'y'
        if c == 'q': newl = newl + 'z'
        if c == ' ': newl = newl + ' '
    
    if case < int(cases):
        newl = newl + '\n'        
    o.write('Case #' + str(case) + ': ' + newl)



o.close()
f.close()


