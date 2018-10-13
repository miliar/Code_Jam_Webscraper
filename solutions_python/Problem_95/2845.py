fin = open("C:\\Users\\t\\Desktop\\a.in","r")

x = int(fin.readline().split('\n')[0])
for i in range(x):
    inp2 = fin.readline().split('\n')
    inp = list(inp2[0])
    out = []
    for c in inp:
        
        if c == 'a':
            out.append('y')
        if c == 'b':
            out.append('h')
        if c == 'c':
            out.append('e')
        if c == 'd':
            out.append('s')
        if c == 'e':
            out.append('o')
        if c == 'f':
            out.append('c')
        if c == 'g':
            out.append('v')
        if c == 'h':
            out.append('x')
        if c == 'i':
            out.append('d')
        if c == 'j':
            out.append('u')
        if c == 'k':
            out.append('i')
        if c == 'l':
            out.append('g')
        if c== ' ':
            out.append(' ')
              
        if c == 'm':
            out.append('l')
        if c == 'n':
            out.append('b')
        if c == 'o':
            out.append('k')
        if c == 'p':
            out.append('r')
        if c == 'q':
            out.append('z')
        if c == 'r':
            out.append('t')
        if c == 's':
            out.append('n')
        if c == 't':
            out.append('w')
        if c == 'u':
            out.append('j')
        if c == 'v':
            out.append('p')
        if c == 'w':
            out.append('f')
        if c == 'x':
            out.append('m')
        if c == 'y':
            out.append('a')
        if c == 'z':
            out.append('q')

    print "Case #"+str(i+1)+": "+''.join(out)
    
