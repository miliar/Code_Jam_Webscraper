import operator
for case in range(input()):
    turnaround = input()
    NA, NB = map(int, raw_input().split())
    schedule = [] 
    for trip in range(NA + NB):
        line = map(int, raw_input().replace(':', ' ').split(' '))
        schedule.append({'start': line[0] * 60 + line[1], 'finish': line[2] * 60 + line[3] + turnaround, 'direction':  trip < NA})
    schedule.sort(key=operator.itemgetter('start'))
    trains = []
    A, B = 0, 0 
    for trip in schedule:
        new_train = True
        for train in trains:
            if train['station'] != trip['direction'] and train['time'] <= trip['start']:
                train['time'] = trip['finish']
                train['station'] = not train['station']
                new_train = False
                break
        if new_train:
            trains.append({'time': trip['finish'], 'station': trip['direction']})
            if trip['direction']: A = A + 1
            else: B = B + 1     
    print 'Case #%s: %s' % (case + 1, str(A) + ' ' + str(B))
