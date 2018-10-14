import sys

def next_line():
    return sys.stdin.readline()

def read_case():
    return [float (i) for i in next_line().split()]

def do_case(C, F, X):
    t, speed = 0.0, 2.0
    last_tf = X
    while True:
        tf = t + X / speed
        tn = t + C / speed
        if tf > last_tf:
            return last_tf
        elif tf < tn:
            return t + tf
        else:
            last_tf = tf
            t = tn
            speed = speed + F





n_cases = int(next_line())
case = 1
for i in range(n_cases):
    # C, F, X
    current = read_case()
    reply = do_case(current[0], current[1], current[2])
    print "Case #%i: %s" % (case, reply)
    case = case + 1
