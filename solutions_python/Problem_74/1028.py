BIG = 65537

IN = 'A-large.in'

def getGoal(who, goals):
    return goals[who].pop(0) if len(goals[who]) > 0 else (BIG, 0)

with open(IN, 'r') as fin:
    with open('a.out', 'w') as fout:
        lines = fin.readlines()

        T = int(lines[0])

        count = 0
        for case in lines[1:]:
            count += 1
            what = case.split()[1:]
            what = [(what[i], int(what[i + 1])) for i in xrange(0, len(what), 2)]
#            print what

            goals = {}
            goals['O'] = [(i, what[i][1]) for i in xrange(len(what)) if what[i][0] == 'O']
            goals['B'] = [(i, what[i][1]) for i in xrange(len(what)) if what[i][0] == 'B']

            pos = {}
            pos['O'] = 1
            pos['B'] = 1

            goal = {}
            goal['O'] = getGoal('O', goals)
            goal['B'] = getGoal('B', goals)

            time = 0
            where = 0
            for j in xrange(len(what)):
                seek = 'O' if goal['O'][0] < goal['B'][0] else 'B'
                wait = 'O' if seek == 'B' else 'B'

                seekDist = abs(goal[seek][1] - pos[seek])
                waitDist = abs(goal[wait][1] - pos[wait])

                if seekDist >= waitDist - 1:
                    pos[wait] = goal[wait][1]
                else:
                    pos[wait] += (seekDist + 1) * int.__cmp__(goal[wait][1], pos[wait])

                pos[seek] = goal[seek][1]
                goal[seek] = getGoal(seek, goals)                   
                    
#                print 'k', seekDist
                time += seekDist + 1

#            print 'Case #%d: %d\n' % (count, time)
            fout.write('Case #%d: %d\n' % (count, time))
