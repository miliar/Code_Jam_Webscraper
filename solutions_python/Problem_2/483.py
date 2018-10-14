def plus_minute(s):
    if s=='23:59':
        return '00:00'
    elif s[-2:] == '59':
        t = str(int(s[:2])+1)
        t = '0'*(2-len(t))+t
        return t+':'+'00'
    else:
        t = str(int(s[-2:])+1)
        t = '0'*(2-len(t))+t
        return s[:2]+':'+t

f = open('largein.txt')
trains_a,trains_b=[],[]
cases = []
k = 0
for l in f:
    k += 1
    if len(l)<4 and k>1:
        cases.append([int(l)])
    elif k>1:
        if len(l)<9:
            x = l.split(' ')
            cases[-1].append(int(x[0]))
            cases[-1].append(int(x[1]))
        else:
            x = l.split(' ')
            cases[-1].append([x[0],x[1].replace('\n','')])
f.close()

q = 0
for i in cases:
    turnaroundsa = []
    turnaroundsb = []
    q += 1
    turnaround = i[0]
    na=i[1]
    if type(na)!=int: print i
    nb=i[2]
    atob = i[3:3+na]
    atob.sort()
    a_b_departures = [j[0] for j in atob]
    a_b_arrivals = [j[1] for j in atob]
    btoa = i[3+na:]
    btoa.sort()
    b_a_departures = [j[0] for j in btoa]
    b_a_arrivals = [j[1] for j in btoa]
    start = i[3:]
    start.sort()
    time = start[0][0]
    start_trains = [0,0]
    trains = [0,0]
    if time == '00:00':
        if atob[0][0] == '00:00':
            start_trains[0]+=a_b_departures.count('00:00')
        if btoa[0][0] == '00:00':
            start_trains[1]+=b_a_departures.count('00:00')
        time = plus_minute(time)
    while time > '00:00':
        for z in range(len(turnaroundsa)):
            turnaroundsa[z] -= 1
            if turnaroundsa[z] == 0:
                trains[0]+=1
        for z in range(len(turnaroundsb)):
            turnaroundsb[z] -= 1
            if turnaroundsb[z] == 0:
                trains[1]+=1            
        if time in a_b_arrivals:
            for y in range(a_b_arrivals.count(time)):
                turnaroundsb.append(turnaround)
                if turnaroundsb[-1] == 0:
                    trains[1]+=1
        if time in b_a_arrivals:
            for y in range(b_a_arrivals.count(time)):
                turnaroundsa.append(turnaround)
                if turnaroundsa[-1] == 0:
                    trains[0]+=1
        if time in b_a_departures:
            if trains[1]>=b_a_departures.count(time):
                trains[1]-=b_a_departures.count(time)
            else:
                start_trains[1]+=b_a_departures.count(time)-trains[1]
                trains[1] = 0
        if time in a_b_departures:
            if trains[0]>=a_b_departures.count(time):
                trains[0]-=a_b_departures.count(time)
            else:
                start_trains[0]+=a_b_departures.count(time)-trains[0]
                trains[0] =0
        time = plus_minute(time)
    print 'Case #'+str(q)+': '+str(start_trains[0])+' '+str(start_trains[1])
