n = int(raw_input(''))

for p in range(n):
    ookisa = raw_input('').split()
    height = int(ookisa[0])
    width = int(ookisa[1])
    maps = []
    
    for h in range(height + 2):
        if h == 0 or h == height+1:
            for w in range(width+2):
                maps.append('.')
        else:
            maps.append('.')
            maps.extend( list( raw_input('') ) )
            maps.append('.')

    #print maps
    #for h in range(height):
    #    for w in range(width):
    #        print maps[(1+h)*(width+2)+(w+1)],
    #    print ''

    flag = 0
    for i in range((height+2)*(width+2)):
        if maps[i] == '.' or maps[i] == '/' or maps[i] == '\\':
            # do nothing
            1
        elif maps[i] == '#':
            maps[i] = '/'
            if (maps[i+1] == '#' and maps[i+width+2] == '#' and maps[i+width+2+1] == '#'):
                maps[i+1] = '\\'
                maps[i+width+2] = '\\'
                maps[i+width+2+1] = '/'
            else:
                print '''Case #%d:''' % (p+1)
                print 'Impossible'
                flag = 1
                break

    if flag == 0:
        print '''Case #%d:''' % (p+1)
        for h in range(height):
            line = ''
            for w in range(width):
                line = line + maps[(1+h)*(width+2)+(w+1)]
            print line
    

