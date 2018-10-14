import sys

T = int(sys.stdin.readline())

for _t in xrange(T):

    bots = {'O':1,'B':1}
    line = sys.stdin.readline().split()
    N = line.pop(0)
    #print N, line

    dest = [[],[]]
    order = []
    while len(line) > 0:
        if line[0] == 'O':
            order.append('O')
            dest[0].append(int(line[1]))
        elif line[0] == 'B':
            order.append('B')
            dest[1].append(int(line[1]))
        line.pop(0)
        line.pop(0)
    #print dest

    nb_buttons_pressed = 0
    secs = 1
    
    while len(order) > 0:
        #print "secs: ", secs
        button_pressed = 0
        if len(dest[0]) > 0 and bots['O'] != dest[0][0]:
            if bots['O'] < dest[0][0]:
                bots['O'] += 1
            elif bots['O'] > dest[0][0]:
                bots['O'] -= 1
        else:
            if len(order) > 0 and order[0] == 'O':
                nb_buttons_pressed += 1
                dest[0].pop(0)
                order.pop(0)
                button_pressed = 1
        if len(dest[1]) > 0 and bots['B'] != dest[1][0]:
            if bots['B'] < dest[1][0]:
                bots['B'] += 1
            elif bots['B'] > dest[1][0]:
                bots['B'] -= 1
        else:
            if len(order) > 0 and order[0] == 'B' and button_pressed == 0:
                nb_buttons_pressed += 1
                dest[1].pop(0)
                order.pop(0)                    
        secs += 1
        #print bots, order, dest, nb_buttons_pressed, N                        
    print "Case #%d: %d" % (_t+1, secs - 1)

        
