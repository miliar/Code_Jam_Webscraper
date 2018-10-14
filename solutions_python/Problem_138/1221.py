'''
Created on 12/04/14 
Code Jam 2014 QR D
@author: manolo
'''
import copy

import sys
ifile = sys.stdin
ofile = open('./d.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))

def find_minimum_heavier_wood(woods, other_wood, name):
    for i in range(len(woods)):
        if woods[i] > other_wood:
#            print '{} takes wood with weigth = {} and wins a point'.format(name, woods[i])
            return i
#    print '{} takes wood with weigth = {} and wins a point'.format(name, woods[0])
    return 0

T = int(r())
for case in range(1,T+1):

    N = int(r())
    naomi = [float(f) for f in r().split(' ')]
    ken = [float(f) for f in r().split(' ')]
    
    naomi2 = copy.copy(naomi)
    ken2 = copy.copy(ken)
    
    # WAR
    ken.sort()
#    print 'N = {}'.format(N)
#    print 'naomi = {}'.format(naomi)
#    print '  ken = {}'.format(ken)
#    print '------------------------------------------'
    points_war = 0
    for wood_naomi in naomi:
        i_ken = find_minimum_heavier_wood(ken, wood_naomi, 'ken')
        if wood_naomi > ken[i_ken]:
            points_war += 1
        ken.pop(i_ken)
        
#    print 'war: {}'.format(points_naomi)
    
    
    # DEC
    naomi2.sort()
#    print 'N = {}'.format(N)
#    print 'naomi2 = {}'.format(naomi2)
#    print '  ken2 = {}'.format(ken2)
#    print '------------------------------------------'
    points_dec = 0
    for wood_ken in ken2:
        i_naomi = find_minimum_heavier_wood(naomi2, wood_ken, 'naomi')
        if wood_ken < naomi2[i_naomi]:
            points_dec += 1
        naomi2.pop(i_naomi)
        
#    print 'dec: {}'.format(points_naomi)
    
    
#    print '___________________________________________\n'

    w(case, '{} {}'.format(points_dec, points_war))


ofile.close

