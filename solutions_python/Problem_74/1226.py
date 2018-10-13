'''
author: prasun kumar gupta
id: prasunkgupta@gmail.com
nick: ppkkgg
date: may 7, 2011
lang: Python 2.7.1
'''

def find_next_pos(list, curr, robot):
    endofline = len(list)-1
    if curr >= endofline:
        return 0            #finished
    for i in range(curr, endofline, 2):
        if list[i] == robot:
            return int(list[i+1])
    return 0
    
f = file('C:\Docume~1\Administrator\MyDocu~1\Downloads\\A-large.in')
o = file('C:\Docume~1\Administrator\MyDocu~1\Downloads\\A-large.out', 'w')
line = f.readline()
T = int(line)
for case in range(1, T+1):
    time = 0L
    line = f.readline()
    line = line.split(' ')
    look = 1
    curr_opos = 1
    curr_bpos = 1
    has_opress = 1
    has_bpress = 1
    whos_job = ''
    print line
    while True:
        next_opos = find_next_pos(line, look, 'O')
        next_bpos = find_next_pos(line, look, 'B')
        try:
            whos_job = line[look]
        except:
            whos_job = ''
##        print look
##        print 'curr_opos', curr_opos,
##        print 'next_opos', next_opos
##        print 'has_opress', has_opress        
##        print 'curr_bpos', curr_bpos,
##        print 'next_bpos', next_bpos
##        print 'has_bpress', has_bpress
        if next_opos != 0 and curr_opos < next_opos:
            curr_opos += 1
            has_opress = 0
        elif next_opos != 0 and curr_opos > next_opos:
            curr_opos -= 1
            has_opress = 0
        elif whos_job == 'O' and next_opos != 0 and curr_opos == next_opos:
            has_opress = 1
            look += 2
        if next_bpos != 0 and curr_bpos < next_bpos:
            curr_bpos += 1
            has_bpress = 0
        elif next_bpos != 0 and curr_bpos > next_bpos:
            curr_bpos -= 1
            has_bpress = 0
        elif whos_job == 'B' and next_bpos != 0 and curr_bpos == next_bpos:
            has_bpress = 1
            look += 2
##        print look
##        print 'curr_opos', curr_opos,
##        print 'next_opos', next_opos
##        print 'has_opress', has_opress        
##        print 'curr_bpos', curr_bpos,
##        print 'next_bpos', next_bpos
##        print 'has_bpress', has_bpress
        if next_opos == 0 and next_bpos == 0 and has_opress == 1 and has_bpress == 1:
            break
        time += 1
    o.write('Case #%d: %d\n' %(case, time))
o.close()
f.close()









