f = open('C:/temp/input.txt', 'r')
a = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
class point:
    altitude = 0
    orient = ''
    type = 0

    
nbMaps = int(f.readline()[:-1])

numMap = 1

while numMap <= nbMaps:
    print 'Case #%d:' % numMap
       
    line = f.readline()
    line = line.split()
    height = int(line[0])
    width = int(line[1])
    
    map = [[point() for col in range(width)] for row in range(height)]
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listTypes = range(26)
    
    for i in range(height):
        line = f.readline()
        line = line.split()
        
        for j in range(width):
            map[i][j].altitude = int(line[j])


    for i in range(height):
        for j in range(width):


            n = 10001
            e = 10001
            s = 10001
            o = 10001
        
            if (i>0):
                n = map[i-1][j].altitude

            if (j< width-1):
                e = map[i][j+1].altitude

            if (i<height-1):
                s = map[i+1][j].altitude

            if (j>0):
                o = map[i][j-1].altitude
            minimum = min([n,s,e,o,10001])
            #print n,e,s,o
            #print minimum
            #print 'ok'
    
            
            if s == minimum: orient = 's'
            if e == minimum : orient = 'e'
            if o == minimum : orient = 'o'
            if n == minimum : orient = 'n'
            if map[i][j].altitude <= minimum: orient = 'fond'
            map[i][j].orient = orient
            
  
    for i in range(height):
        for j in range(width):
            if map[i][j].orient == 'fond':
                map[i][j].type = listTypes.pop(0)

    repeat = 1
    for i in range(1000):
        repeat = 0
        for i in range(height):
            for j in range(width):
                if map[i][j].type == 0:
                    repeat = 1
                    if map[i][j].orient == 'n':
                        map[i][j].type = map[i-1][j].type
                        
                    if map[i][j].orient == 'e':
                        map[i][j].type = map[i][j+1].type
                        
                    if map[i][j].orient == 's':
                        map[i][j].type = map[i+1][j].type
                        
                    if map[i][j].orient == 'o':
                        map[i][j].type = map[i][j-1].type

    types = [0 for i in range(26)]
    for i in range(height):
            for j in range(width):
                if types[map[i][j].type] == 0:
                    types[map[i][j].type] = alphabet.pop(0)
                    
                

    for i in range(height):
            for j in range(width):
                
                if (j == width-1):
                    print types[map[i][j].type]
                else:
                    print types[map[i][j].type],

    numMap += 1

