from sys import stdin
from sys import stdout

def north(h, w, x):
    return (x-w >= 0 and [x-w] or [None])[0]

def west(h, w, x):
    return (x%w > 0 and [x-1] or [None])[0]

def east(h, w, x):
    return (x%w < w-1 and [x+1] or [None])[0]

def south(h, w, x):
    return (x+w < h*w and [x+w] or [None])[0]

moves = [north, west, east, south]

inp = stdin.read()
(t, inp) = inp.split(None, 1)

for case in range(1, int(t) + 1):
    (h, w, inp) = inp.split(None, 2)
    h = int(h)
    w = int(w)
    m = inp.split(None, h*w)
    inp = m[-1]
    m = m[:h*w]
    
    l = [""] * h * w
    nextSink = "a"

    while "" in l:
        q = [l.index("")]
        while True:
            if l[q[-1]] != "": break
            min = q[-1]
            for move in moves:
                x = move(h, w, q[-1])
                if x is not None and m[x] < m[min]: min = x
            if min == q[-1]:
                break
            else:
                q.append(min)
        if l[q[-1]] == "":
            sink = nextSink
            nextSink = chr(ord(nextSink)+1)
        else:
            sink = l[q[-1]]
        while len(q) > 0: l[q.pop()] = sink
    
    print "Case #%d:" % case
    print "\n".join([" ".join(l[i:i+w]) for i in range(0, h*w, w)])