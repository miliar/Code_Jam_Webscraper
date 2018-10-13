events = [] # (time, type ("A"|"D"), where ("A"|"B"))

def parse_time(s):
    h, m = s.split(":")
    return int(h)*60 + int(m)

def parse_line(line, frm):
    t1, t2 = map(parse_time, line[:-1].split())
    if frm == "A":
        events.append((t1, "D", "A"))
        events.append((t2 + turn, "A", "B"))
    else:
        events.append((t1, "D", "B"))
        events.append((t2 + turn, "A", "A"))

def sim():
    global events
    events.sort()
    station = {"A":0, "B":0}
    extreme = {"A":0, "B":0}
    
    for t, type, where in events:
        if type == "D":
            station[where] -= 1
            if station[where] < extreme[where]:
                extreme[where] = station[where]
        else:
            station[where] += 1
    
    print -extreme["A"], -extreme["B"]

f = file("B-large.in.txt")
n = int(f.readline())
for i in range(n):
    events = []
    turn = int(f.readline())
    na, nb = map(int, f.readline().split())
    while na > 0:
        parse_line(f.readline(), "A")
        na -= 1
    while nb > 0:
        parse_line(f.readline(), "B")
        nb -= 1
    print "Case #%d:" % (i+1),
    sim()
