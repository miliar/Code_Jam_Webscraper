import time, datetime, sys

class TestCase(object):

    def __init__(self, events):
        self.events = events

    def computeTrainsRequired(self):
        events = sorted(self.events, cmp=sortEvents)
        location_train_count = {"a": 0, "b": 0}
        initial_trains_by_location = {"a": 0, "b": 0}
        for time, event, location in events:#Make sure events is sorted by time
            if event is "train_ready":
                location_train_count[location] += 1 #There's another train here.
            elif event is "departure":
                if location_train_count[location] <= 0:
                    initial_trains_by_location[location] += 1
                else:
                    location_train_count[location] -= 1 #A train just left
        return initial_trains_by_location

def sortEvents(a, b):
    if a[0] == b[0]: #Time's are the same
        if a[1] is "train_ready" and b[1] is "departure":
            return -1
        elif a[1] is "departure" and b[1] is "train_ready":
            return 1
        else:
            return 0
    return cmp(a[0], b[0])

def makeEvents(location, events, turnaround_time):
    the_events = []
    start_location = location
    if location is "a":
        end_location = "b"
    else:
        end_location = "a"
    turnaround_delta = datetime.timedelta(minutes = turnaround_time)
    for event_pair in events:
        departure, arrival = event_pair.split()
        d_time = time.strptime(departure, "%H:%M")[3:5]
        a_time = datetime.datetime.strptime(arrival, "%H:%M")

        the_events.append((d_time, "departure", start_location))

        train_ready = a_time + turnaround_delta
        train_ready_time = (train_ready.hour, train_ready.minute)
        
        the_events.append((train_ready_time, "train_ready", end_location))

    return the_events                 

def readTestCases(lines):
    test_cases = []
    test_case_count = int(lines[0])
    lines = lines[1:]
    while len(test_cases) < test_case_count:
        events = []
        turnaround_time = int(lines[0])
        a_b_count, b_a_count = map(int, lines[1].split())
        event_lines = lines[2:2 + a_b_count + b_a_count]
        events.extend(makeEvents("a", event_lines[:a_b_count], turnaround_time))
        events.extend(makeEvents("b", event_lines[a_b_count:], turnaround_time))
        test_cases.append(TestCase(events))
        lines = lines[2 + a_b_count + b_a_count:]
    return test_cases

def processInputFile(filepath):
    data = open(filepath, "r").read()
    lines = data.split("\n")
    return readTestCases(lines)

if __name__ == "__main__":
    cases = processInputFile(sys.argv[1])
    case_count = 0
    for case in cases:
        case_count += 1
        trains_required = case.computeTrainsRequired()
        print "Case #%d: %d %d" % (case_count, trains_required["a"], trains_required["b"])
