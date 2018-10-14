import sys
import datetime
import psyco

def findindex(a, time):
    b = [i for i in a]
    c = min(b)
    while time > c:
        b.pop(b.index(c))
        c = min(b)
    return a.index(c)

def change(loc):
    if loc == 'a':
        return 'b'
    else:
        return 'a'

def solution(astart, aend, bstart, bend, T):
    delta = datetime.timedelta(minutes=T)
    sa = 0
    sb = 0
    schedule = dict()
    schedule['astart'] = astart
    schedule['aend'] = aend
    schedule['bstart'] = bstart
    schedule['bend'] = bend
    while astart != [] or bstart != []:
        if astart != []:
            amin = min(astart)
        else:
            amin = datetime.datetime.max
        if bstart != []:
            bmin = min(bstart)
        else:
            bmin = datetime.datetime.max
        if amin < bmin:
            handle = amin
            sa += 1
            index = astart.index(amin)
            astart.pop(index)
            time = aend.pop(index) + delta
            location = 'b'
            while schedule[location + 'start'] != [] and time <= max(schedule[location + 'start']):
                index = findindex(schedule[location + 'start'], time)
                schedule[location + 'start'].pop(index)
                time = schedule[location + 'end'].pop(index) + delta
                location = change(location)
        if bmin < amin:
            handle = bmin
            sb += 1
            index = bstart.index(bmin)
            bstart.pop(index)
            time = bend.pop(index) + delta
            location = 'a'
            while schedule[location + 'start'] != [] and time <= max(schedule[location + 'start']):
                index = findindex(schedule[location + 'start'], time)
                schedule[location + 'start'].pop(index)
                time = schedule[location + 'end'].pop(index) + delta
                location = change(location)
        if bmin == amin:
            aendmin = min(aend)
            bendmin = min(bend)
            if aendmin < bendmin:
                handle = amin
                sa += 1
                index = astart.index(amin)
                astart.pop(index)
                time = aend.pop(index) + delta
                location = 'b'
                while schedule[location + 'start'] != [] and time <= max(schedule[location + 'start']):
                    index = findindex(schedule[location + 'start'], time)
                    schedule[location + 'start'].pop(index)
                    time = schedule[location + 'end'].pop(index) + delta
                    location = change(location)
            if bendmin <= aendmin:
                handle = bmin
                sb += 1
                index = bstart.index(bmin)
                bstart.pop(index)
                time = bend.pop(index) + delta
                location = 'a'
                while schedule[location + 'start'] != [] and time <= max(schedule[location + 'start']):
                    index = findindex(schedule[location + 'start'], time)
                    schedule[location + 'start'].pop(index)
                    time = schedule[location + 'end'].pop(index) + delta
                    location = change(location)
    return sa, sb

def main():
    # use datetime
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day


    file = open(sys.argv[1], 'r')
    nc = int(file.readline())

    count = 1
    for case in range(nc):
        T = int(file.readline())
        na, nb = file.readline().split()
        na = int(na)
        nb = int(nb)
        astart = []
        aend = []
        bstart = []
        bend = []
        for i in range(na):
            tmpline = file.readline().split()
            tmptime = tmpline[0].split(':')
            astart.append(datetime.datetime(year, month, day, int(tmptime[0]), int(tmptime[1])))
            tmptime = tmpline[1].split(':')
            aend.append(datetime.datetime(year, month, day, int(tmptime[0]), int(tmptime[1])))
        for j in range(nb):
            tmpline = file.readline().split()
            tmptime = tmpline[0].split(':')
            bstart.append(datetime.datetime(year, month, day, int(tmptime[0]), int(tmptime[1])))
            tmptime = tmpline[1].split(':')
            bend.append(datetime.datetime(year, month, day, int(tmptime[0]), int(tmptime[1])))
        sa, sb = solution(astart, aend, bstart, bend, T)
        print 'Case #' + str(count) + ':', sa, sb

        count += 1

if __name__ == "__main__":
    #g = psyco.proxy(main)
    #g()
    main()
