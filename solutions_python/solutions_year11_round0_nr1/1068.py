n_cases = input()

for case in xrange(1, n_cases + 1):
    bot = {'O': [1, 0], 'B': [1, 0]}
    
    buttons = raw_input().split()[1:]
    buttons = zip(buttons[::2], map(int, buttons[1::2]))

    time = 0
    
    for color, pos in buttons:
        last_pos, last_time = bot[color]
        time += 1 + max(0, abs(pos - last_pos) - (time - last_time))
        bot[color] = [pos, time]
        
    print "Case #%d: %d" % (case, time)
