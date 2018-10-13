n = int(raw_input())

def convert_time(t):
    hour, min = map(int, t.split(':'))
    return hour*60+min

for i in range(n):
    trains = {'a': 0, 'b': 0}
    needed = {'a': 0, 'b': 0}
    t = int(raw_input())
    na, nb = map(int, raw_input().split())

    timetable = []

    for _ in range(na):
        dep, arr = map(convert_time, raw_input().split())
        arr += t
        timetable.append((dep, 'dep', 'a'))
        timetable.append((arr, 'arr', 'b'))
    
    for _ in range(nb):
        dep, arr = map(convert_time, raw_input().split())
        arr += t
        timetable.append((dep, 'dep', 'b'))
        timetable.append((arr, 'arr', 'a'))
    
    timetable.sort()

    for time, kind, place in timetable:
        if kind == 'dep':
            if trains[place] > 0:
                trains[place] -= 1
            else:
                needed[place] += 1
        else:
            assert kind == 'arr'
            trains[place] += 1

    print 'Case #%i: %i %i' % (i+1, needed['a'], needed['b'])
