f = open('input.txt');
o = open('output.txt', 'w');
T = int(f.readline());

casenum = 1;
for line in f:
    strdata = line.split();
    N = int(strdata[0]);
    strdata = strdata[1::];
    buttons = [];
    for i in xrange(0,len(strdata), 2):
        buttons.append( (strdata[i], int(strdata[i+1])) );
        
    Obuttons = [elem[1] for elem in filter(lambda x: x[0] == 'O', buttons)];
    Bbuttons = [elem[1] for elem in filter(lambda x: x[0] == 'B', buttons)];
    if Obuttons == []:
        seconds = Bbuttons[0];
        for i in xrange(1,len(Bbuttons)):
            seconds += abs(Bbuttons[i] - Bbuttons[i-1]) + 1;
        o.write("Case #"+str(casenum)+": "+str(seconds)+"\n");
        casenum += 1;
        continue;
    if Bbuttons == []:
        seconds = Obuttons[0];
        for i in xrange(1,len(Obuttons)):
            seconds += abs(Obuttons[i] - Obuttons[i-1]) + 1;
        o.write("Case #"+str(casenum)+": "+str(seconds)+"\n");
        casenum += 1;
        continue;
    
    ConditionsAchieved = [];
    
    OrangeCur = 1;
    BlueCur = 1;
    OrangeNextIndex = 0;
    BlueNextIndex = 0;
    OrangeDone = False;
    BlueDone = False;
    seconds = 0;
    while len(ConditionsAchieved) < len(buttons):
        #o.write( 'enable: ' + buttons[ len(buttons) - len(ConditionsAchieved) - 1][0] + '\n');
        #o.write( 'orange now at '+ str(OrangeCur) + ' trying to get to ' + str(Obuttons[OrangeNextIndex]) + '\n');
        #o.write( 'blue now at ' + str(BlueCur) + ' trying to get to ' + str(Bbuttons[BlueNextIndex]) + '\n');
        PressButton = False;
        if buttons[ len(ConditionsAchieved)][0] == 'O':
            OrangePress = True;
            BluePress = False;
        else:
            OrangePress = False;
            BluePress = True;
            
        if not OrangeDone:
            if OrangeCur < Obuttons[OrangeNextIndex]:
                OrangeCur += 1;
            elif OrangeCur > Obuttons[OrangeNextIndex]:
                OrangeCur -= 1;
            else:
                if OrangePress:
                    OrangeNextIndex += 1;
                    PressButton = True;
                    if OrangeNextIndex == len(Obuttons):
                        OrangeDone = True;
                        OrangeNextIndex -=1;
                    
        if not BlueDone:
            if BlueCur < Bbuttons[BlueNextIndex]:
                BlueCur += 1;
            elif BlueCur > Bbuttons[BlueNextIndex]:
                BlueCur -= 1;
            else:
                if BluePress:
                    BlueNextIndex += 1;
                    PressButton = True;
                    if BlueNextIndex == len(Bbuttons):
                        BlueDone = True;
                        BlueNextIndex -= 1;
        if PressButton:
            ConditionsAchieved.append(True);
        seconds += 1;
    
    o.write("Case #"+str(casenum)+": "+str(seconds)+"\n");
    casenum += 1;
    
f.close();
o.close();