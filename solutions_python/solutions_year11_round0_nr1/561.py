from sys import argv

f = open( argv[1] )
for i in xrange(int(f.readline())):
    
    line = f.readline().split()
    moves = [ (line[2*j+1],int(line[2*j+2])) for j in xrange(int(line[0])) ]
    
    j = 0
    t = 0
    blue = orange = 1
    while j < len(moves):    
        t += 1
        push = False
        a = b = j
        
        while a != len(moves) and moves[a][0] != 'O':
            a += 1
        while b != len(moves) and moves[b][0] != 'B':
            b += 1
        
        if a != len(moves):            
            if moves[a][1] > orange:
                orange += 1
            elif moves[a][1] < orange:
                orange -= 1
            else:
                if a == j:
                    push = True
        
        if b != len(moves):         
            if moves[b][1] > blue:
                blue += 1
            elif moves[b][1] < blue:
                blue -= 1
            else:
                if b == j:
                    push = True
                     
        if push:
            j += 1

    print "Case #"+str(i+1)+": "+str(t)
f.close()
