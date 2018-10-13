from datetime import *
(A,B)=range(2)
(ARRIVE,DEPART)=range(-1,2,2)

strptime = lambda str : datetime.strptime(str, "%H:%M")
readfromline = lambda func : (func(input) for input in str(raw_input()).split())
def maketimelist(station, count, turnaround):
    list=[]
    for y in range(count):
        depart, arrive = readfromline(str)
        list.append([(strptime(depart),station),DEPART])
        list.append([(strptime(arrive)+turnaround,(station+1) % 2),ARRIVE])
    return list

def merge_duplicate_times(events):
    ret=[]
    last_event=None
    for x in range(len(events)):
        if events[x][0]==last_event:
            ret[-1][1]+=events[x][1]
        else:
            ret.append(events[x])
            last_event=ret[-1][0]
    return ret
        

if __name__ == '__main__':
    n=int(raw_input())
    for x in range(n):
        t=timedelta(minutes=int(raw_input()))
        na, nb = readfromline(int)
        events = maketimelist(A,na,t)
        events.extend(maketimelist(B,nb,t))
        events.sort()
        events=merge_duplicate_times(events)
        
        needed = [0, 0]
        current = [0, 0]
        for event in events:
            station=event[0][1]
            current[station]+=event[1]
            needed[station]=max(needed[station],current[station])
        print 'Case #'+str(x+1)+': '+str(needed[A])+' '+str(needed[B])