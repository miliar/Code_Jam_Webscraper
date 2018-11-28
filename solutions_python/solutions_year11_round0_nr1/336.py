filename = 'A-large';
fin = open(filename + '.in', 'r')
out = open(filename + '.out', 'w')

T = int(fin.readline())

for t in range(1, T+1):
    l = fin.readline().split(' ')
    N = int(l.pop(0))
    
    
    bots = {'B': 1, 'O': 1}
    
    # jobs = {'B': None, 'O': None}
    
    current = 0
    time = 0
    
    while current < 2*N - 1:
        bot = l[current]
        button = int(l[current+1])
        
        if bot == 'B':
            secondbot = 'O'
        else:
            secondbot = 'B'
        
        
        # move bot to button and press
        steptime = abs(button - bots[bot]) + 1
        time += steptime
        
        bots[bot] = button
        
        
        if current < 2*N - 3:
            #second move to button
            i = current + 2
            secondbotjob = -1
            while i < 2*N - 1:
                if l[i] == secondbot: 
                    secondbotjob = i
                    break
                i += 2
            

            if secondbotjob > -1:
                togo = int(l[i+1]) - bots[secondbot]
                steps = min(steptime, abs(togo))
                if togo < 0:
                    steps *= -1
                
                bots[secondbot] += steps
    
        current += 2
    
    out.write('Case #%d: %d\n' % (t, time))
