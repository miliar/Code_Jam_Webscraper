#!/usr/bin/env python
from __future__ import division
import sys

def solve(in_array):
    rpi_arr = []
    wp, wp_cal = [],0.0
    owp, owp_cal = [],0.0
    oowp, oowp_ca = [],0.0
    g_played = []
    for i in xrange(0, len(in_array)):
        count = 0
        wp.append(0.0)
        owp.append(0.0)
        oowp.append(0.0)
        for j in xrange(0, len(in_array[i])):
            if in_array[i][j] == '1' or in_array[i][j] == '0':
                count += 1
        g_played.append(count)
        

    for i in xrange(0, len(in_array)):
        for j in xrange(0, len(in_array[i])):
            if in_array[i][j] == '1':
                wp[i] += 1/g_played[i]
        round(wp[i],12)
    #print wp
    '''cal oowp
    '''
    for i in xrange(0, len(in_array)):
        for j in xrange(0, len(in_array[i])):
            if in_array[i][j] != '.':
                won = g_played[j] * wp[j]
                if in_array[j][i] == '1':
                    won -= 1
                rev_wp = won / (g_played[j]-1)
                owp[i] += rev_wp / g_played[i]
        round(owp[i], 12)
    #print owp
    for i in xrange(0, len(in_array)):
        for j in xrange(0, len(in_array)):
            if in_array[i][j] != '.':
                oowp[i] += owp[j]/g_played[i]
        round(oowp[i],12)
    #print oowp
    
    for i in xrange(0, len(in_array)):
        rpi_arr.append((0.25*wp[i])+ (0.5*owp[i]) + (0.25*oowp[i]))    
    return rpi_arr


if __name__ == "__main__":
    in_array = []
    results = []
    infile = open('A-large.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        teams = int(infile.readline())
        for j in xrange(0, teams):
            in_array.append([])
            in_array[j].extend(infile.readline().strip('\n'))
        results.append([])
        results[i].extend(solve(in_array))
        in_array = []
    infile.close()

    for result in xrange(0,len(results)):
        outfile.write(("Case #%d:\n") % (result+1))
        for j in xrange(0,len(results[result])):
            outfile.write(str(results[result][j])+'\n')
    outfile.close()
