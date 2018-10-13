
def ggt(events):
    def inner_ggt(a, b):
        mult, remainder = divmod(a, b)
        while remainder:
            a = b
            b = remainder
            mult, remainder = divmod(a, b)
        return abs(b)
    distances = []
    for event in events[1:]:
        distances.append(events[0] - event)
    return abs(reduce(inner_ggt, distances))

def sanity(events, increment, result):
    for event in events:
        assert divmod(event + result, increment)[1] == 0

count = int(raw_input())
i = 1

while i <= count:
    events = map(int, raw_input().split())
    raw_events = events[1:]
    events = []
    for event in raw_events:
        if event not in events:
            events.append(event)
    
    increment = ggt(events)
    latest = max(events)
    remainder = divmod(latest, increment)[1]
    if not remainder:
        result = 0
    else:
        result = increment - divmod(latest, increment)[1]
    sanity(events, increment, result)
    print 'Case #%i: %s' % (i, result)
    i += 1
