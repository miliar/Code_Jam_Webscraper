## code jam competition 2008
## train timetable

inputf = open('B-large.in','r')
outputf = open('B-large.out','w')

lines = inputf.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
N = int(lines[0])
line = 1

for case in range(1,N+1):
    T = int(lines[line])
    [NA, NB] = lines[line+1].split(' ')
    [NA, NB] = [int(NA), int(NB)]
    ABtrips = lines[line+2:line+2+NA]
    BAtrips = lines[line+2+NA:line+2+NA+NB]
    for i in range(NA):
        ABtrips[i] = {'dep': {'hr': int(ABtrips[i][:2]),\
                              'min': int(ABtrips[i][3:5])},\
                      'arr': {'hr': int(ABtrips[i][6:8]),\
                              'min': int(ABtrips[i][9:11])}}
    for i in range(NB):
        BAtrips[i] = {'dep': {'hr': int(BAtrips[i][:2]),\
                              'min': int(BAtrips[i][3:5])},\
                      'arr': {'hr': int(BAtrips[i][6:8]),\
                              'min': int(BAtrips[i][9:11])}}
    line += 2 + NA + NB

    ## all parsed

    times = []
    for i in range(NA):
        times.append((ABtrips[i]['dep']['hr']*60 + ABtrips[i]['dep']['min'], 'depA'))
        times.append((ABtrips[i]['arr']['hr']*60 + ABtrips[i]['arr']['min'] + T, 'arrB'))
    for i in range(NB):
        times.append((BAtrips[i]['dep']['hr']*60 + BAtrips[i]['dep']['min'], 'depB'))
        times.append((BAtrips[i]['arr']['hr']*60 + BAtrips[i]['arr']['min'] + T, 'arrA'))

    times.sort()
    [countA, countB] = [0,0]
    [minA, minB] = [0,0]

    for time in times:
        if time[1] == 'depA':
            countA -= 1
            if countA < minA:
                minA = countA
        elif time[1] == 'depB':
            countB -= 1
            if countB < minB:
                minB = countB
        elif time[1] == 'arrA':
            countA += 1
        elif time[1] == 'arrB':
            countB += 1

    outputf.write('Case #%d: %d %d\n' % (case, -minA, -minB))

inputf.close()
outputf.close()
