ifile = open('../input/A-large.in', 'r')
ofile = open('../output/A-large.out', 'w')

cases = int(ifile.readline())

for case in xrange(cases):
    bots = {
      'B': dict(seconds=0, button=1),
      'O': dict(seconds=0, button=1),
    }
    color = None     
    for token in ifile.readline().split()[1:]:        
        if color is None:
            color = token
            continue
        button = int(token)
        other = 'O' if color == 'B' else 'B' 
        #move + push 
        move = abs(bots[color]['button'] - button)
        bots[color]['seconds'] = max(bots[color]['seconds'] + move, bots[other]['seconds']) + 1
        bots[color]['button'] = button                
        color = None
    seconds = max(bots['O']['seconds'], bots['B']['seconds'])
    #print seconds
    ofile.write('Case #%d: %d\n' % (case+1, seconds))
