#!/usr/bin/env python3.1
with open('A-large.in', 'r') as f:
    line = f.readline()
    times = int(line)
    for case in range(1, times + 1):
        line = f.readline()
        fields = line.split()
        times2 = int(fields[0])
        i = times2
        oTasks = []
        oPlace =  1
        bPlace =  1
        bTasks = []
        sequence = []
        for j in range(i):
            if fields[j*2 + 1] in 'O':
                sequence.append(0)
                oTasks.append(int(fields[j*2 + 2]))
            else:
                sequence.append(1)
                bTasks.append(int(fields[j*2 + 2]))
        time = 0

        while len(sequence) is not 0:

            if sequence[0] is 0:
                if len(bTasks) is not 0:
                    if bPlace < bTasks[0]:
                        bPlace = bPlace + 1
                    elif bPlace > bTasks[0]:
                        bPlace = bPlace - 1
                if oPlace < oTasks[0]:
                    oPlace = oPlace + 1
                elif oPlace > oTasks[0]:
                    oPlace = oPlace - 1
                else:
                    del sequence[0]
                    del oTasks[0]
            else:
                if len(oTasks) is not 0:
                    if oPlace < oTasks[0]:
                        oPlace = oPlace + 1
                    elif oPlace > oTasks[0]:
                        oPlace = oPlace - 1
                if bPlace < bTasks[0]:
                    bPlace = bPlace + 1
                elif bPlace > bTasks[0]:
                    bPlace = bPlace - 1
                else:
                    del sequence[0]
                    del bTasks[0]
            time = time + 1
        print('Case #{0}: {1}'.format(case, time))
