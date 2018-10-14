f = file("B-large.in")
cases = int(f.readline(),10)

def addhr(tt, of):
    thr = tt.split(':')
    mins = int(thr[1])+of
    hr = int(thr[0])
    if mins>=60:
        hr += 1
        mins -= 60
    return (hr * 100)+mins
    

for i in range(cases):
    turna = int(f.readline(),10)
    nab = f.readline().split(' ')
    na = int(nab[0],10)
    nb = int(nab[1],10)
    stations = { 'a':[], 'b':[] }
    tab = []
    for ia in range(na):
        tt = f.readline().split(' ')
        trip = (int(tt[0].replace(':','')),addhr(tt[1],turna), 'ab')
        tab.append(trip)
    for ia in range(nb):
        tt=f.readline().split(' ')
        trip = (int(tt[0].replace(':','')),addhr(tt[1],turna), 'ba')
        tab.append(trip)

    tab.sort()

    #print tab
    
    count = { 'a' : 0, 'b':0}
    for t in tab:
        trains = stations[t[2][0]]
        for tri in range(len(trains)):
            if t[0]>=trains[tri]:
                stations[t[2][0]] = trains[:tri]+trains[tri+1:]
                break            
        else:
            count[t[2][0]] += 1

        stations[t[2][1]].append(t[1])
        #print stations

    print "Case #%s: %s %s" % (i+1, count['a'],count['b'])
        
        
