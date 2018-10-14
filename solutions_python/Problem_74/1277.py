#!/usr/bin/env python
#
import re 
import math
inputfile = open("input.dat",'r')
lines = inputfile.readlines()
inputfile.close()
output = open("output.dat",'w')
orangelist = []
bluelist = []
for i in range(1,len(lines)):
    splitline = re.split('\s',lines[i])
    for j in range(1,len(splitline)-1,2):
        if splitline[j] == 'O':
             orangelist.append(int(splitline[j+1]))
        else:
             bluelist.append(int(splitline[j+1]))
    print 'orange list: ' + str(orangelist)+ ' '
    print 'blue list: '   + str(bluelist)  + ' '
    print 'full list: '   + str(splitline) + ' '
    if bluelist == []:
         bluelist.append(1)
    if orangelist == []:
         orangelist.append(1)
    time = 0 
    done = 0
    opos = 1
    bluepos = 1
    pressindex = 0
    iorangenext = 0
    ibluenext = 0
    lastpress = int(splitline[0])
    onext = int(orangelist[0])
    bluenext = int(bluelist[0])
    nextpress = splitline[1]
    while done == 0:
        pressed = 0
        print 'time is:' + str(time)
        if opos != onext:
             opos = opos + (onext - opos)/abs(onext - opos)
             print '   orange moved to button:' + str(opos)
             print '   orange going to:' + str(onext)
        elif opos == onext:
             print ' orange waiting at button: ' + str(opos)
             if nextpress == 'O':
                  print ' orange pressing button: ' + str(opos)
                  pressed = 1
                  if iorangenext < len(orangelist)-1:
                       iorangenext = iorangenext + 1
                       onext = orangelist[iorangenext]
        if bluepos != bluenext:
            bluepos = bluepos +  (bluenext - bluepos)/abs(bluenext - bluepos)
            print '   blue moved to button:' + str(bluepos)
            print '   blue going to:' + str(bluenext)
        elif bluepos == bluenext:
            print ' blue waiting at button: ' + str(bluepos)
            if nextpress == 'B':
                print ' blue pressing button: ' + str(bluepos)
                pressed = 1
                if ibluenext < len(bluelist)-1:
                     ibluenext = ibluenext + 1
                     bluenext = bluelist[ibluenext]
        print ' buttons left to be pressed: ' + str(lastpress - pressindex)
        if pressed == 1:
            pressindex = pressindex + 1
            nextpress = splitline[pressindex*2+1]
        if pressindex == lastpress:  
            done = 1
        time = time + 1
 #           done = 1
    output.write('Case #' + str(i) + ': ' + str(time) + '\n')
    orangelist[:] = []
    bluelist[:]   = []
output.close()

