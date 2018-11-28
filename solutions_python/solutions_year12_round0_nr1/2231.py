import sys
file = sys.argv[1]
input = open(file,'r')

def translator(char):
    result = ' '
    if char == 'a':
        result = 'y'
    
    if char == 'b':
        result = 'h'

    if char == 'c':
        result = 'e'
    
    if char == 'd':
        result = 's'
    
    if char == 'e':
        result = 'o'

    if char == 'f':
        result = 'c'
    
    if char == 'g':
        result = 'v'
    
    if char == 'h':
        result = 'x'

    if char == 'i':
        result = 'd'
    
    if char == 'j':
        result = 'u'
    
    if char == 'k':
        result = 'i'

    if char == 'l':
        result = 'g'
        
    if char == 'm':
        result = 'l'

    if char == 'n':
        result = 'b'
        
    if char == 'o':
        result = 'k'

    if char == 'p':
        result = 'r'
    
    if char == 'q':
        result = 'z'
    
    if char == 'r':
        result = 't'

    if char == 's':
        result = 'n'
    
    if char == 't':
        result = 'w'
    
    if char == 'u':
        result = 'j'

    if char == 'v':
        result = 'p'

    if char == 'w':
        result = 'f'
    
    if char == 'x':
        result = 'm'
    
    if char == 'y':
        result = 'a'

    if char == 'z':
        result = 'q'
    
    return result

t = int(input.readline())
# there are n test cases, we will loop over t cases

for i in range(t):
    googlerese = input.readline()
    translated = ''
	    
    #we will loop over each character in googlerese and replace with tranlator
    for j in range(len(googlerese)):
        char = googlerese[j]
        translated = translated + translator(char)

    print "Case #" + str(i+1)+": " + translated
