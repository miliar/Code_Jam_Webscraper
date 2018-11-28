'''Cookie Solver'''
import sys

def cookie_solver(c, f, x):

    cookies_sec = 2.0
    cookies = 0.0
    seconds = 0.0
    
    while cookies < x:
        seconds_to_win = (x - cookies) / cookies_sec
        seconds_to_factory = c / cookies_sec

        if seconds_to_win < seconds_to_factory:
            return seconds + seconds_to_win
        else:
            seconds += seconds_to_factory
            cookies += seconds_to_factory * cookies_sec
            if ((x - cookies) / cookies_sec) > (x / (cookies_sec + f)):
                cookies -= c
                cookies_sec += f

    return seconds

with open(sys.argv[1], 'r') as goog_inp:
    data_sets = int(goog_inp.readline())
    with open('B.out', 'w') as bout:
        for case, data in enumerate(xrange(0, data_sets)):
            floats = map(float, goog_inp.readline().split())
            c, f, x = floats[0], floats[1], floats[2]
            bout.write('Case #' + str(case + 1) + ': %.7F \n' % cookie_solver(c, f, x))
        

