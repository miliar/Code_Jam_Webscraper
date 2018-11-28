#!/usr/bin/python

infile = open('bot.in', 'r')
outfile = open('bot.out', 'w')

t = int(infile.readline())

for i in range(0, t):
    elements = infile.readline().split(' ')
    elements.reverse()
    n = int(elements.pop())
    
    map = {'O': {'pos': 1, 'time': 0}, 'B': {'pos': 1, 'time': 0}}
    
    prev_bot = ''
    curr_time = 0
    for j in range(0, n):
        bot = elements.pop()
        position = int(elements.pop())
        
        if map[bot]['pos'] == position:
            map[bot]['time']+=1
        else:
            map[bot]['time']+= abs(position-map[bot]['pos'])+1
            map[bot]['pos'] = position
            
        if prev_bot != bot:
            if bot == 'O' and map['B']['time'] >= map['O']['time']:
                map[bot]['time'] = map['B']['time']+1
            elif bot == 'B' and map['O']['time'] >= map['B']['time']:
                map[bot]['time'] = map['O']['time']+1
        
        prev_bot = bot
        curr_time = max(map['O']['time'], map['B']['time'])
    
    print "Case #"+str(i+1)+": "+str(curr_time)
    outfile.write("Case #"+str(i+1)+": "+str(curr_time)+"\n")
    