fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

t = int(fin.readline())
for x in range(t):
    data = fin.readline().split(' ')
    n = int(data[0])
    data = data[1:]

    pos = {'O': 1, 'B': 1}
    color = data[0]
    time = 0
    redtime = 0

    splist = []
    # for every step... do this
    for y in range(0,n*2,2):
        r = data[y]
        p = int(data[y+1])

        if color == r:
            pass
        else:
            splist.append([color,time,redtime])
            color = r
            redtime = abs(pos[color] - p)
            time = 0
        time += abs(pos[color] - p)
        time += 1
        pos[color] = p
        
    splist.append([color,time,redtime])

    #use splist to count the time taken
    for y in range(len(splist)-1):
        splist[y+1][1] -= min(splist[y][1], splist[y+1][2])
    totaltime= 0
    for step in splist:
        totaltime += step[1]
    print('Case #'+str(x+1)+': '+str(totaltime), file=fout)
            
         
            
fout.close() 
fin.close()
