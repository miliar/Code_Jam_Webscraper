'''
Created on Apr 13, 2012

@author: Shan
'''



charmap = {}
charmap['a'] = 'y'
charmap['b'] = 'h'
charmap['c'] = 'e'
charmap['d'] = 's'
charmap['e'] = 'o'
charmap['f'] = 'c'
charmap['g'] = 'v'
charmap['h'] = 'x'
charmap['i'] = 'd'
charmap['j'] = 'u'
charmap['k'] = 'i'
charmap['l'] = 'g'
charmap['m'] = 'l'
charmap['n'] = 'b'
charmap['o'] = 'k'
charmap['p'] = 'r'
charmap['q'] = 'z' ###
charmap['r'] = 't'
charmap['s'] = 'n'
charmap['t'] = 'w'
charmap['u'] = 'j'
charmap['v'] = 'p'
charmap['w'] = 'f'
charmap['x'] = 'm'
charmap['y'] = 'a'
charmap['z'] = 'q' ###
charmap[' '] = ' '

def translate(gstr):
    '''
    return translated string
    '''
    chars = list(gstr)
    out = ''
    #print chars
    for c in chars:
        #print c
        ochar = charmap.get(c)
        if ochar:
            out += ochar 
    
    
    return out

f = open('input.txt', 'r')
lines = f.readlines()

count =  int(lines[0])

counter = 1
while counter <= count:
    line = lines[counter]
    
    
    print "Case #"+str(counter)+": " + translate(line)
    counter +=1

f.close()