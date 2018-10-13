import sys

sys.stdin.readline()
case = 0
while 1:
    contra = { 'O': 'B', 'B': 'O' }
    free = {'O': 0, 'B': 0 }
    pos = { 'O': 1, 'B': 1 }
    actions = { 'O': [], 'B': [] }
    times = []
    sequence = []
    time = 0
    line = sys.stdin.readline()
    if not line:
        break
    parts = line.split( ' ' )
    parts.remove(parts[0])
    lastr = ''
    for i in range(0,len(parts)-1,2):
        r,p = parts[i], int(parts[i+1])
        actions[r].append(p)
        sequence.append(r)

    times.append({})
    while len(actions['O']) + len(actions['B']) > 0:
        r = sequence[0]
        p = actions[r][0]
        time += 1
        times.append({'O':'','B':''})
        if( pos[r] == p ):
            times[time][r] = 'Push Button'
            actions[r].remove(p)
            sequence.remove(r)
        elif pos[r] < p:
            pos[r] += 1
            times[time][r] = str(pos[r]) + ' Walk to Button ' + str(p)
        else:
            pos[r] -= 1
            times[time][r] = str(pos[r]) + ' Walk to Button ' + str(p)

        r = contra[r]
        if len(actions[r]) == 0 or pos[r] == actions[r][0]:
            times[time][r] = 'Wait at Button '
        elif pos[r] < actions[r][0]:
            pos[r] += 1
            times[time][r] = str(pos[r]) + ' Walk to Button ' + str(actions[r][0])
        else:
            pos[r] -= 1
            times[time][r] = str(pos[r]) + ' Walk to Button ' + str(actions[r][0])
#        print str(time) + " " + times[time]['O'] + " | " + times[time]['B']

    case += 1
    print "Case #%d: %d" % (case, time)
