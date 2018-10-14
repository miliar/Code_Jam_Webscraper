def count(c,f,x,t):
    sofar = 0.0
    mini = x/t
    while(True):
        turns = x/t + sofar
        nextt = c/t + x/(t+f) + sofar
#        print turns,nextt
        if mini > turns:
            mini = turns
        if nextt > mini:
            break
        sofar += c/t
        t += f
    return mini


if __name__ == "__main__":
    cases = int(raw_input())
    
    for case_no in xrange(cases):
        [c,f,x] = map(float,raw_input().strip().split())
        print "Case #" + str(case_no+1) +( ": %.7f"%count(c,f,x,2))
