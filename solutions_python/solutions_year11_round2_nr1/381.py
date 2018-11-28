#encoding: utf-8

import sys

fin = open('%s.in' % sys.argv[1], 'r')
fout = open('%s.out' % sys.argv[1], 'w')

debug = False

def read_number(file):
    return int(file.readline())

def read_number_list(file):
    return [int(n) for n in read_list(file)]

def read_list(file):
    return file.readline().split(' ')

def read_word(file):
    return file.readline().strip()

cases = read_number(fin)

for case in xrange(cases):
    teams = read_number(fin)
    schedule = []
    for i in xrange(teams):
        schedule.append(read_word(fin))

    stats = []

    for i in xrange(teams):
        GP = len([a for a in schedule[i] if a != '.']) * 1.0
        WP = len([a for a in schedule[i] if a == '1']) / GP
        stats.append({'WP' : WP, 'GP' : GP})

    for i in xrange(teams):
        OWP = 0
        te = 0
        for t in xrange(teams):
            if t == i or schedule[t][i] == '.' : continue
            te += 1
            WPsI = (stats[t]['WP'] * stats[t]['GP'] - int(schedule[t][i])) / (stats[t]['GP'] - 1)
            OWP += WPsI

        stats[i]['OWP'] = OWP / te

    GOOWP = 0
    for i in xrange(teams):
        OOWP = 0
        te = 0
        for t in xrange(teams):
            if t == i or schedule[t][i] == '.' : continue
            te += 1
            OOWP += stats[t]['OWP']
        stats[i]['OOWP'] = OOWP / te

    for i in xrange(teams):
        st = stats[i]
        st['RIP'] = 0.25 * st['WP'] + 0.5 * st['OWP'] + 0.25 * st['OOWP']

    if debug :
        for i,st in enumerate(stats):
            print "Team %d: WP = %.6f OWP = %.6f OOWP = %.6f" % (i, st['WP'], st['OWP'], st['OOWP'])
    
    response = '\n' + '\n'.join(['%.12f' % st['RIP'] for st in stats])

    #Output
    print ("Case #%d:" % (case + 1)) + response
    fout.write("Case #%d: %s\n" % (case + 1, response))
