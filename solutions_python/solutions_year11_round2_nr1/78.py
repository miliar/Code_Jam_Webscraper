#!/usr/bin/env python

import sys
import numpy

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        nteams = int(f.readline().strip())

        games = []
        for i in xrange(nteams) :
            games.append(f.readline().strip())

        ngames = numpy.zeros(nteams, int)
        nwins  = numpy.zeros(nteams, int)

        wp = numpy.zeros(nteams)
        owp = numpy.zeros(nteams)

        nri = numpy.zeros(nteams)
        
        opponents = []
        for i in xrange(nteams) :
            opponents.append([])
            for j in xrange(nteams) :
                if not games[i][j] == '.' :
                    opponents[-1].append(j)
                    ngames[i] += 1
                    if games[i][j] == '1' :
                        nwins[i] += 1

        for i in xrange(nteams) :
            wp[i]  = float(nwins[i])/float(ngames[i])
            sum_owp = 0.0
            for o in opponents[i] :
                if games[i][o] == '0' :
                    sum_owp += float(nwins[o]-1)/float(ngames[o]-1)
                else :
                    sum_owp += float(nwins[o])/float(ngames[o]-1)
            owp[i] = sum_owp / len(opponents[i])

        for i in xrange(nteams) :
            oowp = sum(owp[opponents[i]]) / len(opponents[i])
            nri[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp
                       
        print 'Case #%i:'%(icase+1)
        for i in xrange(nteams) :
            print nri[i]
    
    f.close()

main()
