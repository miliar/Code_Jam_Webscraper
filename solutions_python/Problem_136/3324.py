# |C| BugOS
# http://code.google.com/codejam/contest/1836486/dashboard#s=p2&a=2
import itertools

def simulate(C, F, X):
    #C: Farm Price
    #F: Farm Cookies per Second
    #X: Wanted Cookies

    t = 0. #Time
    f = 2. #Cookies per Second
    
    while is_efficient(f):
        #buy and update
        t = t + C / f #mazevoume arketa mpiskota me tin proigoumeni apodosi
        f = f + F #anevazoyme thn apodosh agorazontas

    return t + X / f

def is_efficient(f):
    cookies_needed = X - C
    time_needed = cookies_needed / f
    return time_needed * F > C

def output(test_case, time):
    more_dec_places = repr(time)
    print "Case #%d: %s" % (test_case, more_dec_places)

#Input
fin = open('large.in', 'r')
fin.readline()
for test_case, line in enumerate(fin, 1):
    line = map(float, line.split())
    C, F, X = line
    time = simulate(C, F, X)
    output(test_case, time)
