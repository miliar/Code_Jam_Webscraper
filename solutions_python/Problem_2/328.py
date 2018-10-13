class event_data(object):
    def __init__(self,side,departs,sim_time):
        #print "Creating event:",side,departs,sim_time/60,":",sim_time%60
        self.side = side
        self.departs = departs
        self.sim_time = sim_time
    
    def __cmp__(self,other):
        if self.sim_time == other.sim_time:
            return cmp(self.departs,other.departs)
        return cmp(self.sim_time, other.sim_time)
    
    def __repr__(self):
        return "< Event: side %s, departs: %r, time: %d:%d>" % (self.side,self.departs,self.sim_time/60,self.sim_time%60)


OTHER_SIDE = {"a":"b","b":"a"}

class stations_state(object):
    def __init__(self):
        self.total_trains = {"a":0,"b":0}
        self.available_trains = {"a":0,"b":0}


def handle_event(state,event):
    #print "Handling event: ", event
    side = event.side
    state.available_trains[side] += (1,-1)[event.departs == True]
    if state.available_trains[side] < 0:
        state.available_trains[side] += 1
        state.total_trains[side] += 1
        if state.available_trains[side] < 0:
            exit("INVALID STATE!")

def hhmm_to_int(hhmm):
    (hh,mm) = hhmm.split(":")
    return int(hh)*60+int(mm)

def parse_line(side,events_list,line,turn_around):
    (depart,arrive) = line.split(" ")
    events_list.append(event_data(side,True,hhmm_to_int(depart)))
    events_list.append(event_data(OTHER_SIDE[side],False,hhmm_to_int(arrive)+turn_around))

def solve_table(na,nb,rail_times_lines,turn_around):
    events = []
    state = stations_state()
    if na + nb != len(rail_times_lines):
        exit("INVALID INPUT!")
    side = "a"
    for i in range(len(rail_times_lines)):
        if i == na:
            side = OTHER_SIDE[side]
        parse_line(side,events,rail_times_lines[i].strip(),turn_around)
    #print events
    events.sort()
    #print events
    for event in events:
        handle_event(state,event)
    return state.total_trains

def handle_case(lines):
    turn_around = int(lines.pop(0))
    (na,nb) = lines.pop(0).strip().split(" ")
    na = int(na)
    nb = int(nb)
    rail_times_lines = lines[0:(na+nb)]
    del lines[0:(na+nb)]
    return solve_table(na,nb,rail_times_lines,turn_around)

import sys

lines = file(sys.argv[1]).readlines()
cases_count = int(lines[0])
lines = lines[1:]
current_line = 1
for case_count in range(1,cases_count+1):
    solution = handle_case(lines)
    print "Case #%d: %d %d" % (case_count, solution["a"],solution["b"])
