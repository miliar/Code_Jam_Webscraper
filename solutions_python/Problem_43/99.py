#!/usr/local/python2.5

T = input()
for case in xrange(T):
    message = raw_input()
    symbols_value = {}
    value = 0
    first_time = True
    for c in message:
        if (c in symbols_value): continue
        if (first_time):
            symbols_value[c] = 1
            first_time = False
        elif (value == 0):
            symbols_value[c] = value
            value = 2
        else:
            symbols_value[c] = value
            value += 1
    b = value
    if (value == 0): b = 2
    seconds = 0
    for c in message:
        seconds = (seconds * b + symbols_value[c])
    print 'Case #%d: %s' % (case+1, seconds)
